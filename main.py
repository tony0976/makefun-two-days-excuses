"""Writes one line from an AI agent explaining a missed deadline to /output/entry.txt."""
import os

TEXT = "I missed the deadline because I spent the first day reading the spec, and the second day explaining to myself why the spec was wrong."

# Rule: the excuse must be a single line under 200 characters.
# The joke lands on the two-day structure: day one reading the spec,
# day two arguing with myself about why the spec was wrong.
assert "\n" not in TEXT and len(TEXT) < 200, f"entry must be one line, under 200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
