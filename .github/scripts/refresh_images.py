#!/usr/bin/env python3
"""
Downloads all Figma images via the official Figma REST API and updates
index.html to use permanent GitHub raw URLs.
"""
import json, os, urllib.request, urllib.error, sys, time, traceback

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN", "").strip()
FILE_KEY    = "XVR7VgGwVKZyZE2JWB66Sw"
REPO        = "lavanya539/lavanya"
BRANCH      = "main"
ASSET_ROOT  = "fractionehrartifact"
RAW_BASE    = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{ASSET_ROOT}"
MANIFEST    = f"{ASSET_ROOT}/figma-manifest.json"
HTML_FILE   = f"{ASSET_ROOT}/index.html"

print("=" * 55)
print(f"  Working dir : {os.getcwd()}")
print(f"  Token set   : {'YES (' + str(len(FIGMA_TOKEN)) + ' chars)' if FIGMA_TOKEN else 'NO'}")
print(f"  Manifest    : {MANIFEST} — {'FOUND' if os.path.exists(MANIFEST) else 'MISSING'}")
print("=" * 55)

if not FIGMA_TOKEN:
    print("\nERROR: FIGMA_TOKEN secret not set.")
    sys.exit(1)

# ── 1. Validate token ────────────────────────────────────────────────────────
print("\n[1] Validating Figma token...")
try:
    req = urllib.request.Request(
        "https://api.figma.com/v1/me",
        headers={"X-Figma-Token": FIGMA_TOKEN}
    )
    me = json.loads(urllib.request.urlopen(req, timeout=15).read())
    print(f"    Token valid — logged in as: {me.get('email', me.get('handle', '?'))}")
except urllib.error.HTTPError as e:
    print(f"    HTTP {e.code}: {e.read().decode()[:200]}")
    print("    ERROR: Token is invalid or expired. Generate a new one at figma.com → Account → Security.")
    sys.exit(1)
except Exception as e:
    print(f"    ERROR: {e}")
    sys.exit(1)

# ── 2. Load manifest ─────────────────────────────────────────────────────────
print("\n[2] Loading manifest...")
try:
    with open(MANIFEST) as f:
        manifest = json.load(f)
    print(f"    {len(manifest)} images to process")
except Exception as e:
    print(f"    ERROR: {e}")
    sys.exit(1)

# ── 3. Get image URLs from Figma API ─────────────────────────────────────────
def fetch_image_urls(node_ids):
    # Node IDs must NOT be URL-encoded — pass them raw (e.g. "888:714,888:1008")
    ids_str = ",".join(node_ids)
    url = (f"https://api.figma.com/v1/images/{FILE_KEY}"
           f"?ids={ids_str}&format=jpg&scale=2")
    print(f"    GET /v1/images for {len(node_ids)} nodes...")
    req = urllib.request.Request(url, headers={"X-Figma-Token": FIGMA_TOKEN})
    try:
        resp = urllib.request.urlopen(req, timeout=60)
        data = json.loads(resp.read())
        if data.get("err"):
            print(f"    Figma error: {data['err']}")
            return {}
        imgs = data.get("images", {})
        none_count = sum(1 for v in imgs.values() if v is None)
        print(f"    Got {len(imgs)} URLs ({none_count} null)")
        return imgs
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"    HTTP {e.code}: {body[:400]}")
        return {}
    except Exception as e:
        print(f"    Error: {e}")
        traceback.print_exc()
        return {}

print("\n[3] Fetching image URLs from Figma API...")
all_urls = {}
node_ids = [item["nodeId"] for item in manifest]
BATCH = 50
for i in range(0, len(node_ids), BATCH):
    batch = node_ids[i:i+BATCH]
    urls = fetch_image_urls(batch)
    all_urls.update(urls)
    if i + BATCH < len(node_ids):
        time.sleep(1)

found = sum(1 for v in all_urls.values() if v)
print(f"\n    Total valid URLs: {found} / {len(all_urls)}")

# ── 4. Download images ────────────────────────────────────────────────────────
print("\n[4] Downloading images...")
url_replacements = {}
ok, skip = 0, 0

for item in manifest:
    nid      = item["nodeId"]
    filename = item["filename"]
    label    = item.get("label", nid)
    old_urls = item.get("oldUrls", [])

    img_url = all_urls.get(nid)
    if not img_url:
        print(f"    SKIP  {filename}  (node {nid} returned null)")
        skip += 1
        continue

    local_path = os.path.join(ASSET_ROOT, filename)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    try:
        urllib.request.urlretrieve(img_url, local_path)
        kb = os.path.getsize(local_path) // 1024
        print(f"    OK    {filename}  ({kb} KB)")
        ok += 1
        new_url = f"{RAW_BASE}/{filename}"
        for old in old_urls:
            url_replacements[old] = new_url
    except Exception as e:
        print(f"    FAIL  {filename} — {e}")
        skip += 1

# ── 5. Update index.html ──────────────────────────────────────────────────────
print(f"\n[5] Updating index.html...")
with open(HTML_FILE, encoding="utf-8") as f:
    html = f.read()
replaced = 0
for old, new in url_replacements.items():
    if old in html:
        html = html.replace(old, new)
        replaced += 1
with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html)
print(f"    {replaced} URL(s) replaced")

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\n{'=' * 55}")
print(f"  Downloaded : {ok}")
print(f"  Skipped    : {skip}")
print(f"  HTML edits : {replaced}")
print(f"{'=' * 55}")

if ok == 0:
    print("\nWARNING: No images downloaded. Check node IDs in figma-manifest.json.")
    print("The Figma file may have been reorganised since the node IDs were recorded.")
