#!/usr/bin/env python3

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
LOCAL_PREFIX = "./assets/exercise-gifs/"
BLOCKED_HOSTS = (
    "https://static.exercisedb.dev/media/",
    "https://raw.githubusercontent.com/",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


html = INDEX.read_text(encoding="utf-8")
gif_urls = re.findall(r'gifUrl:\s*"([^"]+)"', html)

if not gif_urls:
    fail("No gifUrl entries were found in index.html.")

bad_hosts = [url for url in gif_urls if url.startswith(BLOCKED_HOSTS)]
if bad_hosts:
    fail(f"External GIF URLs are not allowed: {bad_hosts[:3]}")

bad_prefix = [url for url in gif_urls if not url.startswith(LOCAL_PREFIX)]
if bad_prefix:
    fail(f"Unexpected GIF path format: {bad_prefix[:3]}")

missing_files = []
for url in gif_urls:
    relative_path = url.removeprefix("./")
    asset_path = ROOT / relative_path
    if not asset_path.exists():
        missing_files.append(str(asset_path))
    elif asset_path.stat().st_size == 0:
        missing_files.append(f"{asset_path} (empty)")

if missing_files:
    fail(f"Missing or empty local GIF assets: {missing_files[:5]}")

unique_urls = len(set(gif_urls))
print(f"Validated {len(gif_urls)} GIF references ({unique_urls} unique local assets).")
