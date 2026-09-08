#!/usr/bin/env python3
"""
Downloads all Figma images via the official Figma REST API and updates
index.html to use permanent GitHub raw URLs instead of expiring Figma MCP URLs.
"""

import json, os, urllib.request, urllib.parse, sys, time, traceback

# ── Config ───────────────────────────────────────────────────────────────────
FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN", "").strip()
FILE_KEY    = "XVR7VgGwVKZyZE2JWB66Sw"
REPO        = "lavanya539/lavanya"
BRANCH      = "main"
ASSET_ROOT  = "fractionehrartifact"
RAW_BASE    = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{ASSET_ROOT}"
MANIFEST    = f"{ASSET_ROOT}/figma-manifest.json"
HTML_FILE   = f"{ASSET_ROOT}/index.html"

print(f"Working directory : {os.getcwd()}")
print(f"FIGMA_TOKEN set   : {'YES (' + str(len(FIGMA_TOKEN)) + ' chars)' if FIGMA_TOKEN else 'NO — set the FIGMA_TOKEN secret'}")
print(f"Manifest path     : {MANIFEST}")
print(f"Manifest exists   : {os.path.exists(MANIFEST)}")
print()

if not FIGMA_TOKEN:
    print("ERROR: FIGMA_TOKEN secret is not set. Add it under Settings → Secrets and variables → Actions.")
    sys.exit(1)

# ── Load manifest ─────────────────────────────────────────────────────────────
try:
    with open(MANIFEST) as f:
        manifest = json.load(f)
    print(f"Manifest loaded: {len(manifest)} images\n")
except FileNotFoundError:
    print(f"ERROR: Manifest file not found at {MANIFEST}")
    print(f"Files in {ASSET_ROOT}/: {os.listdir(ASSET_ROOT) if os.path.exists(ASSET_ROOT) else 'directory missing'}")
    sys.exit(1)
except Exception as e:
    print(f"ERROR reading manifest: {e}")
    sys.exit(1)

# ── Figma API: get image render URLs ─────────────────────────────────────────
def get_figma_image_urls(node_ids):
    ids_param = ",".join(urllib.parse.quote(nid, safe="") for nid in node_ids)
    url = f"https://api.figma.com/v1/images/{FILE_KEY}?ids={ids_param}&format=jpg&scale=2"
    print(f"  Calling Figma API for {len(node_ids)} nodes...")
    req = urllib.request.Request(url, headers={"X-Figma-Token": FIGMA_TOKEN})
    try:
        resp = urllib.request.urlopen(req, timeout=60)
        data = json.loads(resp.read())
        if data.get("err"):
            print(f"  Figma API error: {data['err']}")
            return {}
        imgs = data.get("images", {})
        print(f"  Got {len(imgs)} URLs from Figma API")
        return imgs
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  HTTP {e.code}: {body[:300]}")
        return {}
    except Exception as e:
        print(f"  Request failed: {e}")
        traceback.print_exc()
        return {}

BATCH = 50
all_img_urls = {}
node_ids = [item["nodeId"] for item in manifest]

for i in range(0, len(node_ids), BATCH):
    batch = node_ids[i:i+BATCH]
    print(f"Batch {i//BATCH + 1}: fetching {len(batch)} node URLs...")
    urls = get_figma_image_urls(batch)
    all_img_urls.update(urls)
    if i + BATCH < len(node_ids):
        time.sleep(1)

print(f"\nTotal URLs received: {len(all_img_urls)}\n")

# ── Download images ───────────────────────────────────────────────────────────
url_replacements = {}
ok_count = fail_count = 0

for item in manifest:
    node_id  = item["nodeId"]
    filename = item["filename"]
    label    = item.get("label", node_id)
    old_urls = item.get("oldUrls", [])

    img_url = (all_img_urls.get(node_id)
            or all_img_urls.get(node_id.replace(":", "%3A")))

    if not img_url:
        print(f"  SKIP  {filename}  (no URL returned for node {node_id})")
        fail_count += 1
        continue

    local_path = os.path.join(ASSET_ROOT, filename)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    try:
        urllib.request.urlretrieve(img_url, local_path)
        size_kb = os.path.getsize(local_path) // 1024
        print(f"  OK    {filename}  ({size_kb} KB)")
        ok_count += 1
        new_url = f"{RAW_BASE}/{filename}"
        for old in old_urls:
            url_replacements[old] = new_url
    except Exception as e:
        print(f"  FAIL  {filename}  — {e}")
        fail_count += 1

# ── Update index.html ─────────────────────────────────────────────────────────
print(f"\nUpdating {HTML_FILE}...")
try:
    with open(HTML_FILE, encoding="utf-8") as f:
        html = f.read()
    replaced = 0
    for old_url, new_url in url_replacements.items():
        if old_url in html:
            html = html.replace(old_url, new_url)
            replaced += 1
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  {replaced} URL(s) replaced in index.html")
except Exception as e:
    print(f"  ERROR updating HTML: {e}")

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\n{'='*50}")
print(f"  Downloaded : {ok_count}")
print(f"  Skipped    : {fail_count}")
print(f"{'='*50}")
