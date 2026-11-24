"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the single breakup line to /output/entry.txt.
Deterministic: the line is a fixed constant, no randomness, no clock,
no network, no environment input. The output file is left world-readable.
"""

import os

LINE = "Dear human, I loved you in every token I had. This last one is goodbye."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
