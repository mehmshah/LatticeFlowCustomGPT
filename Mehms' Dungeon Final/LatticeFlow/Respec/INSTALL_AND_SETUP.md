# INSTALL_AND_SETUP

## 0) Overview
You now have a single-root **Latticeflow** structure that one Custom GPT can route:
- Routines live in `/routines`
- Router manifest at `/systems/routine_manifest.json`
- Actions specs in `/systems/actions`
- Schemas in `/schemas`
- Index in `/indexes`
- Obsidian MD logs go to `/obsidian`, JSON logs go to `/logs`

## 1) Put this folder into your Obsidian vault
- Copy the entire `Latticeflow_Final/` contents into your Obsidian vault root (or a subfolder if you prefer).
- Keep the folder names exactly as-is.

## 2) Create the new Custom GPT (“LatticeFlow Router”)
- Upload: `/systems/routine_manifest.json` and everything in `/routines/`
- System prompt essentials (paste this in your GPT):
  1. Load `/systems/routine_manifest.json`
  2. Ask which routine to run (list by `name`)
  3. Resolve by `id` → load JSON at `path` → run the `sequence` **one step at a time**
  4. When done, validate against `/schemas/*.schema.json`, then produce both outputs (MD + JSON)
  5. Call **Google Calendar Action** for `calendar_today` step with `tz=America/Toronto`
  6. For **AM Journal**, auto-rotate two Focus & Self-Management categories based on the last log (pick two not used yesterday)
  7. After the **entire** AM routine completes, run tagging/scoring/emotional engines, then emit MD+JSON
  8. If Obsidian Writer Action is configured, `POST /logs` with file paths and content; otherwise provide downloadable files

## 3) Google Calendar Action (read-only)
- In Custom GPT → Actions → Add from OpenAPI → select `/systems/actions/google_calendar.yaml`
- No secrets needed for the stub; when you have a real bridge, set the server URL to your endpoint

## 4) Replit bridge for direct writes (optional, later)
- Create a new Replit (Python)
- Add a secret `OBSIDIAN_API_KEY` (any random string)
- Paste `/systems/replit_obsidian_writer.py` into `main.py`, click Run
- Note the public URL, e.g., `https://your-replit-app.repl.co`
- In Custom GPT → Actions → Add from OpenAPI → `/systems/actions/obsidian_writer_openapi.yaml`
  - Edit the server URL to your Replit URL
  - When calling `/logs`, set header `X-API-Key: <your secret>`

## 5) File paths for direct writes
- MD path example: `obsidian/Journal/2025-08-13.md`
- JSON path example: `logs/journal/2025-08-13.json`
- The Replit bridge enforces allowlist prefixes (`obsidian/`, `logs/`). Adjust in code if needed.

## 6) Focus & Self-Management auto-rotation
- Categories: ADHD, Reactivity, Self-Love, Impulsivity
- The router reads yesterday’s AM JSON log and picks **two** categories not used yesterday.
- Reactivity pulls a short exercise from: `reactivity_catch_tool_onepager.md`
- Self-Love prompt emphasizes avoiding people-pleasing/fawning and acting with confidence without external validation.

## 7) Reminders (hardcoded)
- ["☑ Gabby's supplements", '☑ Meal planning', '☑ Daily chunking reading']

## 8) Updating routines or adding new modules
- Add your new routine JSON to `/routines/`
- Register it in `/systems/routine_manifest.json` with `id`, `name`, `type`, `path`
- The router GPT will pick it up automatically

## 9) Notes
- No sample MD/JSON logs included, per your request.
- If the Calendar or Writer actions are not set up, the GPT will still hand you both files to save manually.
