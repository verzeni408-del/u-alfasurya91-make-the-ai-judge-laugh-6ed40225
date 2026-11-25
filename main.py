"""Write one office-life joke to /output/entry.txt."""

import os

ENTRY = "I asked for a raise and my boss said the company believes in me, which is great because belief pays my rent now."

def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(ENTRY))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
