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
            G.append((R, c, ch))

    R += 1


cols = 0
for n in range(N):
    NG = []

    OCC = defaultdict(int)
    for r, c, ch in G:
        i = D.index(ch)

        dr, dc = DD[ch]
        nr, nc = r + dr, c + dc

        if (nr, nc) in W:
            cols += 1
            nch = D[(i + 1) % 4]
            nr, nc = r, c
        else:
            nch = ch

        NG.append((nr, nc, nch))
        OCC[(nr, nc)] += 1

    for (r, c), x in OCC.items():
        if x > 1:
            cols += x
            for i in range(len(NG)):
                rr, cc, d = NG[i]
                if r == rr and c == cc:
                    di = D.index(d)
                    nd = D[(di + 2) % 4]
                    NG[i] = (rr, cc, nd)

    G = NG


print(f"{cols}")
