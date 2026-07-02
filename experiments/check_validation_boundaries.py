#!/usr/bin/env python3
"""Guard validation probes against paper-specific behavior injection."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / "experiments" / "paper_conditions_probe.py"

FORBIDDEN_PATTERNS = [
    (re.compile(r"\bant\.state\s*=(?!=)"), "Do not force individual ant states in validation probes."),
    (re.compile(r"\bant\.task\s*=(?!=)"), "Do not force individual ant tasks in validation probes."),
    (re.compile(r"\bant\.thresholds\s*=(?!=)"), "Do not rewrite individual decision thresholds in validation probes."),
    (re.compile(r"\bantSim\.[A-Za-z0-9_]+\s*=\s*function"), "Do not monkey-patch simulator API functions in validation probes."),
    (re.compile(r"\bprototype\."), "Do not patch prototypes in validation probes."),
    (re.compile(r"\beval\s*\("), "Do not use eval in validation probes."),
]


def main():
    text = PROBE.read_text(encoding="utf-8")
    failures = []
    for pattern, message in FORBIDDEN_PATTERNS:
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            failures.append(f"{PROBE}:{line}: {message}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print("validation boundary check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
