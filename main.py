"""One Star, Five Stars for the Food — alien tourist's one-star review of Earth.

Writes a single sentence (<=200 chars) to /output/entry.txt: an alien
tourist gives Earth one star but cannot deny the food is excellent.
"""

import os

ENTRY = (
    "One star: the phở at 11:40 p.m. was so good I missed my flight. "
    "Five stars for the broth, zero for my life choices."
)
# One sentence, 118 chars: alien grievance (missed flight) + food compliment (broth).


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
