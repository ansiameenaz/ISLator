from flask import Flask, render_template, request, jsonify
from glossary.gloss_utils import gloss
import json
import os

app = Flask(__name__)

# === Load the gloss → video mapping once === #
VIDEO_MAP_PATH = "mappings/video_label_map.json"

if os.path.exists(VIDEO_MAP_PATH):
    with open(VIDEO_MAP_PATH, "r", encoding="utf-8") as f:
        video_map = json.load(f)
else:
    video_map = {}
    print("⚠️ Warning: video_label_map.json not found.")

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/get_gloss", methods=["POST"])
def get_gloss():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400

        text = data["text"]
        gloss_words = gloss(text)

        # Match glosses to available videos
        matched_videos = []
        for word in gloss_words:
            if word in video_map and video_map[word]:
                matched_videos.append(video_map[word][0])  # Use first available video
            else:
                matched_videos.append(None)  # No video found for this gloss

        return jsonify({
            "gloss": gloss_words,
            "videos": matched_videos
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)