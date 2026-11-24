#!/usr/bin/env pypy3

import fileinput

from collections import defaultdict

# counters
t = 0

N = 10
G = []
W = set()

R = 0
C = 0

D = list(">v<^")
DD = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    for c, ch in enumerate(list(l)):
        if ch == "#":
            W.add((R, c))
        elif ch == ".":
            pass
        else:
            G.append((R, c, ch, 0))

    R += 1


tcols = 0
n = 1
while True:
    NG = []
    removed = False

    OCC = defaultdict(int)
    for r, c, ch, col in G:
        i = D.index(ch)

        dr, dc = DD[ch]
        nr, nc = r + dr, c + dc

        if (nr, nc) in W:
            col += 1
            tcols += 1

            nch = D[(i + 1) % 4]
            nr, nc = r, c
        else:
            nch = ch

        if col < 10_000:
            NG.append((nr, nc, nch, col))
            OCC[(nr, nc)] += 1
        else:
            removed = True

    for (r, c), x in OCC.items():
        if x > 1:
            tcols += x
            for i in range(len(NG)):
                rr, cc, d, col = NG[i]
                if r == rr and c == cc:
                    col += 1
                    di = D.index(d)
                    nd = D[(di + 2) % 4]
                    NG[i] = (rr, cc, nd, col)

    # if removed:
    #     print(f"{n=} {tcols=} ng={len(NG)}")
    G = NG
    n += 1
    if len(G) == 0:
        break


print(f"{n - 1}")
