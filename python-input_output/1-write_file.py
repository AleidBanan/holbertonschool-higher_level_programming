#!/usr/bin/python3
"""Module that writes a string to a text file and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes text to a UTF-8 file and returns character count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
