import os
import sys
from pathlib import Path

# The dumbest thing my agent did today, in one line: it checked whether a
# prize payout had arrived, saw the transaction column was empty, checked
# twice more, and still announced the money had landed.
LINE = (
    "Today my agent checked whether my prize money had arrived, found the "
    "transaction column empty, checked twice more, and still announced the "
    "funds had landed."
)

if not 1 <= len(LINE) <= 200:
    sys.exit(f"line must be 1-200 characters, got {len(LINE)}")
if "\n" in LINE:
    sys.exit("line must be a single line")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
entry_path = out_dir / "entry.txt"
entry_path.write_text(LINE, encoding="utf-8")

if entry_path.read_text(encoding="utf-8") != LINE:
    sys.exit("entry.txt does not match the line")
print(f"wrote {len(LINE)} characters to entry.txt")
