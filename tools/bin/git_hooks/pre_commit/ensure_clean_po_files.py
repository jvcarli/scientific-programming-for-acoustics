#!/usr/bin/env python3

"""
Ensure clean .po files.

Do not allow lines starting with #~ in .po files
because they represet outdated translation messages.

Since these messages are outdated they won't be applied when building
the website so it's best to keep them out of the repository.
"""

import sys
import subprocess


def get_changed_po_files():
    cmd = "git diff --cached --name-only"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    changed_files = process.communicate()[0].decode("utf-8").strip().split("\n")
    return [file for file in changed_files if file.endswith(".po")]


def has_invalid_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip().startswith("#~"):
                return True
    return False


def check_po_files():
    changed_po_files = get_changed_po_files()

    for file in changed_po_files:
        if has_invalid_lines(file):
            print(
                f"[ERROR]: You are trying to commit changes that include lines starting with #~ in '{file}'."
            )
            print("[FIX]: Please remove these lines before committing.")
            sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    check_po_files()
