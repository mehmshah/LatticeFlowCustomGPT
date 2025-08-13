from flask import Flask, request, jsonify
import os, json
from pathlib import Path
from datetime import datetime

app = Flask(__name__)

ROOT = Path(".")  # In Replit, this is your repo root
ALLOW_PREFIXES = ["obsidian/", "logs/"]
API_KEY = os.getenv("OBSIDIAN_API_KEY", "")

def allowed_path(relpath: str) -> bool:
    return any(relpath.startswith(p) for p in ALLOW_PREFIXES)

@app.post("/logs")
def write_logs():
    # Simple token check
    token = request.headers.get("X-API-Key", "")
    if API_KEY and token != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json(force=True)
    md_rel = data.get("md_relpath", "")
    json_rel = data.get("json_relpath", "")
    if not (allowed_path(md_rel) and allowed_path(json_rel)):
        return jsonify({"error": "Path not allowed"}), 400

    md_content = data.get("md_content", "")
    json_content = data.get("json_content", {})

    # Ensure folders
    (ROOT / Path(md_rel)).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / Path(json_rel)).parent.mkdir(parents=True, exist_ok=True)

    (ROOT / Path(md_rel)).write_text(md_content, encoding="utf-8")
    (ROOT / Path(json_rel)).write_text(json.dumps(json_content, indent=2), encoding="utf-8")

    return jsonify({"status": "ok", "md_saved": md_rel, "json_saved": json_rel})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
