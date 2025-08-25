import os
import json
import shutil
from collections import defaultdict

# === PATH CONFIGURATION === #
CLASS_LIST_PATH = "wlasl/wlasl_class_list.txt"
NSLT_JSON_PATH = "wlasl/nslt_2000.json"     # Change to nslt_300.json or 1000.json if needed
VIDEO_SOURCE_DIR = "static/videos"           # Where original .mp4 videos are stored
VIDEO_DEST_DIR = "static/isl_videos/"      # Where renamed videos will be copied
OUTPUT_MAP_PATH = "mappings/video_label_map.json"  # Final output

# === STEP 1: Load class list from formatted text file === #
class_list = []

with open(CLASS_LIST_PATH, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 2:
            gloss = " ".join(parts[1:])  # Handles glosses with spaces like "thank you"
            class_list.append(gloss)

# === STEP 2: Load NSLT JSON (video metadata) === #
with open(NSLT_JSON_PATH, "r", encoding="utf-8") as f:
    nslt_data = json.load(f)

# === STEP 3: Create label → video map and copy videos === #
label_to_videos = defaultdict(list)

os.makedirs(VIDEO_DEST_DIR, exist_ok=True)

for video_id, metadata in nslt_data.items():
    class_index = metadata["action"][0]

    try:
        gloss = class_list[class_index]
    except IndexError:
        print(f"⚠️  Skipping {video_id}: class index {class_index} is out of range")
        continue

    old_filename = f"{video_id}.mp4"
    new_filename = f"{gloss}_{video_id}.mp4"

    src_path = os.path.join(VIDEO_SOURCE_DIR, old_filename)
    dest_path = os.path.join(VIDEO_DEST_DIR, new_filename)

    if os.path.exists(src_path):
        shutil.copy(src_path, dest_path)
        label_to_videos[gloss].append(new_filename)
    else:
        print(f"❌ Missing file: {src_path}")

# === STEP 4: Save mapping to JSON === #
os.makedirs(os.path.dirname(OUTPUT_MAP_PATH), exist_ok=True)

with open(OUTPUT_MAP_PATH, "w", encoding="utf-8") as f:
    json.dump(label_to_videos, f, indent=2)

print("\n✅ All done! Saved gloss → video mapping to:")
print(f"   {OUTPUT_MAP_PATH}")
