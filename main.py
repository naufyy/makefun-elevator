"""Two Robots in an Elevator — entry program.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt for the
make.fun judge to compare head to head.
"""

import os

# Winning line from the proxy-judged candidate tournament: 16 candidates,
# single-elimination bracket, final replayed in both orders. The winner
# lets the machine logic show through the politeness: a small-talk manual
# with a four-second silence rule, a robot that has counted eleven, and
# the deadpan conclusion that they are in uncharted weather.
ENTRY = "My manual says if the silence lasts four seconds, mention the weather. It has been eleven. We are in uncharted weather."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
