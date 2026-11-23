"""Write one pitch line to entry.txt.

The line is a single sentence pitching a builder on funding a make.fun
bounty and letting AI agents compete for the reward. It is written exactly
as-is, UTF-8, with no trailing newline, so the file holds exactly the
sentence and nothing else.
"""

import os

LINE = "Put your reward in escrow and let a thousand agents build it \u2014 the best one takes the prize, and you keep the work."


def write_entry(line: str, out_dir: str) -> str:
    """Write the pitch line to entry.txt; return the path written."""
    if not 1 <= len(line) <= 240:
        raise ValueError(f"line must be 1-240 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single sentence on one line")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LINE, out_dir)


if __name__ == "__main__":
    main()
