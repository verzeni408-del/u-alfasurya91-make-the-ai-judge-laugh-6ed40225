"""One office joke, written to the entry file.

The joke is a single line about office life. The program only writes
that line to /output/entry.txt, nothing else, no network, no extras.
"""

import os


def build_joke():
    opening = "In my exit interview, HR asked what would have made me stay."
    closer = "I said this interview, three years ago."
    return opening + " " + closer


def main():
    joke = build_joke()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(joke)


if __name__ == "__main__":
    main()
