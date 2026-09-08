#!/usr/bin/env python3
"""
Downloads all Figma images via the official Figma REST API and updates
index.html to use permanent GitHub raw URLs instead of expiring Figma MCP URLs.

Reads: fractionehrartifact/figma-manifest.json
Writes: fractionehrartifact/assets/**/*
Updates: fractionehrartifact/index.html
"""

import json, os, urllib.request, urllib.parse, sys, time

# ── Config ──────────────────────────────────────────────────────────────────
FIGMA_TOKEN  = os.environ.get("FIGMA_TOKEN", "")
FILE_KEY     = "XVR7VgGwVKZyZE2JWB66Sw"
REPO         = "lavanya539/lavanya"
BRANCH       = "main"
ASSET_ROOT   = "fractionehrartifact"
RAW_BASE     = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{ASSET_ROOT}"
MANIFEST     = f"{ASSET_ROOT}/figma-manifest.json"
HTML_FILE    = f"{ASSET_ROOT}/index.html"

if not FIGMA_TOKEN:
    print("ERROR: FIGMA_TOKEN environment variable not set.")
    sys.exit(1)

# ── Load manifest ────────────────────────────────────────────────────────────
with open(MANIFEST) as f:
    manifest = json.load(f)

print(f"Manifest loaded: {len(manifest)} images to refresh\n")

# ── Batch Figma API call (max 50 IDs per request) ───────────────────────────
def get_figma_image_urls(node_ids):
    ids_param = ",".join(urllib.parse.quote(nid, safe="") for nid in node_ids)
    url = f"https://api.figma.com/v1/images/{FILE_KEY}?ids={ids_param}&format=jpg&scale=2"
    req = urllib.request.Request(url, headers={"X-Figma-Token": FIGMA_TOKEN})
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        data = json.loads(resp.read())
        if data.get("err"):
            print(f"  Figma API error: {data['err']}")
            return {}
        return data.get("images", {})
    except Exception as e:
        print(f"  Figma API request failed: {e}")
        return {}

BATCH = 50
all_img_urls = {}
node_ids = [item["nodeId"] for item in manifest]
for i in range(0, len(node_ids), BATCH):
    batch = node_ids[i:i+BATCH]
    print(f"Fetching image URLs for nodes {i+1}–{min(i+BATCH, len(node_ids))}...")
    urls = get_figma_image_urls(batch)
    all_img_urls.update(urls)
    time.sleep(0.5)

print(f"\nGot {len(all_img_urls)} image URLs from Figma API\n")

# ── Download images and build replacement map ────────────────────────────────
url_replacements = {}   # { old_figma_url: new_raw_github_url }
ok_count, fail_count = 0, 0

for item in manifest:
    node_id = item["nodeId"]
    filename = item["filename"]
    label    = item.get("label", node_id)
    old_urls = item.get("oldUrls", [])

    # Try the node ID with colon and with URL-encoded colon
    img_url = (all_img_urls.get(node_id)
            or all_img_urls.get(node_id.replace(":", "%3A")))

    if not img_url:
        print(f"  SKIP  {filename}  ({label}) — Figma returned no URL")
        fail_count += 1
        continue

    local_path = os.path.join(ASSET_ROOT, filename)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    try:
        urllib.request.urlretrieve(img_url, local_path)
        size_kb = os.path.getsize(local_path) // 1024
        print(f"  OK    {filename}  ({size_kb} KB)  [{label}]")
        ok_count += 1

        # Register URL replacements
        new_url = f"{RAW_BASE}/{filename}"
        for old in old_urls:
            url_replacements[old] = new_url

    except Exception as e:
        print(f"  FAIL  {filename}  — {e}")
        fail_count += 1

# ── Update index.html ────────────────────────────────────────────────────────
print(f"\nUpdating {HTML_FILE}...")
with open(HTML_FILE, encoding="utf-8") as f:
    html = f.read()

replaced = 0
for old_url, new_url in url_replacements.items():
    if old_url in html:
        html = html.replace(old_url, new_url)
        replaced += 1

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html)

# ── Summary ──────────────────────────────────────────────────────────────────
print(f"\n{'='*50}")
print(f"  Images downloaded : {ok_count}")
print(f"  Images failed     : {fail_count}")
print(f"  HTML replacements : {replaced}")
print(f"{'='*50}")

if fail_count > 0:
    print("\nSome images failed. They will be retried on next run.")
