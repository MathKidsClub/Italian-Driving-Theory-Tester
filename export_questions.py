"""Export AI-enriched questions to questions.js for the quiz web page.

Only rows with ai_review_status='done' are exported. Output is a plain JS file
(window.QUESTIONS = [...]) rather than JSON so the page works when opened
directly from disk (file://), where fetch() of a local file is blocked.

    python TEST/export_questions.py
"""
from __future__ import annotations

import json
import shutil
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "EXTRACT" / "driving_test.sqlite"
EXTRACT_DIR = ROOT / "EXTRACT"
TEST_DIR = Path(__file__).resolve().parent
OUT_PATH = TEST_DIR / "questions.js"
IMAGES_DIR = TEST_DIR / "images"


def parse_key_words(raw: str | None) -> list[dict]:
    pairs = []
    for chunk in (raw or "").split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "=" in chunk:
            phrase, why = chunk.split("=", 1)
            pairs.append({"phrase": phrase.strip(), "why": why.strip()})
        else:
            pairs.append({"phrase": chunk, "why": ""})
    return pairs


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT question_number, question_text, answer, english_translation, "
        "key_words, trick_explanation, image_path "
        "FROM questions WHERE ai_review_status='done' AND COALESCE(question_text,'')<>''"
    ).fetchall()

    IMAGES_DIR.mkdir(exist_ok=True)
    copied = 0
    data = []
    for r in rows:
        image = ""
        if r["image_path"]:
            # copy the referenced image into TEST/images so TEST/ is self-contained
            src = EXTRACT_DIR / r["image_path"]
            name = Path(r["image_path"]).name
            dst = IMAGES_DIR / name
            if src.exists():
                if not dst.exists():
                    shutil.copy2(src, dst)
                    copied += 1
                image = "images/" + name
        data.append(
            {
                "n": r["question_number"],
                "it": r["question_text"],
                "answer": (r["answer"] or "").upper() == "VERO",
                "en": r["english_translation"] or "",
                "keywords": parse_key_words(r["key_words"]),
                "trick": r["trick_explanation"] or "",
                "image": image,
            }
        )
    conn.close()

    OUT_PATH.write_text(
        "window.QUESTIONS = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(data)} questions to {OUT_PATH}")
    print(f"Copied {copied} new image(s) into {IMAGES_DIR}")


if __name__ == "__main__":
    main()
