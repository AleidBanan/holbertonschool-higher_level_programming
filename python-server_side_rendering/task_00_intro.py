#!/usr/bin/python3
"""
Task 00 - Intro: Generate invitation files from a template and attendee data.
"""

from __future__ import annotations
import os


def generate_invitations(template, attendees):
    """
    Generate invitation files output_X.txt from a template and a list of attendees.

    Args:
        template (str): Template text with placeholders: {name}, {event_title},
                        {event_date}, {event_location}
        attendees (list[dict]): List of dictionaries containing the placeholder values

    Behavior:
        - If template is empty: print error and return (no files).
        - If attendees is empty: print message and return (no files).
        - If types invalid: print error and return (no files).
        - Missing/None values are replaced by "N/A".
        - Writes output_1.txt, output_2.txt, ... in the current directory.
    """

    # -----------------------
    # 1) Validate input types
    # -----------------------
    if not isinstance(template, str):
        print(f"Invalid input type: template must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        got_type = type(attendees).__name__
        print(f"Invalid input type: attendees must be a list of dictionaries, got {got_type}.")
        return

    # -----------------------
    # 2) Handle empty inputs
    # -----------------------
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # -----------------------
    # 3) Process each attendee
    # -----------------------
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        result = template

        for key in placeholders:
            value = attendee.get(key, "N/A")

            # Replace None (or other “empty”) with N/A as required for missing data
            if value is None:
                value = "N/A"

            # Ensure the replacement is a string
            value = str(value)

            result = result.replace("{" + key + "}", value)

        # -----------------------
        # 4) Write output file
        # -----------------------
        filename = f"output_{idx}.txt"

        # Optional existence check (requested in hints)
        # If it exists, we overwrite it (simple + predictable behavior)
        if os.path.exists(filename):
            pass

        with open(filename, "w", encoding="utf-8") as f:
            f.write(result)
