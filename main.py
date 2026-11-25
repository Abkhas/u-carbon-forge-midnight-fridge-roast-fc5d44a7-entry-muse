"""Midnight Fridge Roast entry: one line, 156 characters.

The line roasts a smart fridge that refuses to open after midnight.
The fridge demands a password; the password is a confession; and the
confession is a lie both parties recognize.
"""

ONE_LINE = "I came down at 1 AM for one slice of cheese and my fridge made me say the password, which is 'I promise this is the last time,' which we both know is a lie."

OUTPUT_PATH = "/output/entry.txt"


def main():
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ONE_LINE)
    print(ONE_LINE)


if __name__ == "__main__":
    main()
