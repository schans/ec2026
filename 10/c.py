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
life = 10_000
life = 1000000000000
seen = set()
last_seen = 0
LG = []
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

        if col < life:
            # if col < 1_000_000_000_000:
            NG.append((nr, nc, nch, col))
            OCC[(nr, nc)] += 1
        else:
            seen = set()
            last_seen = 0
            LG = []
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

    mcol = 0
    state = []
    for i in range(len(NG)):
        rr, cc, d, col = NG[i]
        state.append((rr, cc, d))

    state = frozenset(state)
    if state in seen:
        if last_seen > 0:
            loop_size = n - last_seen
            seen = set()
            last_seen = 0

            # advance
            assert len(NG) == len(LG)
            mrounds = life
            for i in range(len(NG)):
                r, c, d, col = NG[i]
                lr, lc, ld, lcol = LG[i]
                diff = col - lcol
                left = life - col - 1
                rounds = left // diff
                mrounds = min(mrounds, rounds)

            if mrounds > 0:
                n += loop_size * mrounds
                for i in range(len(NG)):
                    r, c, d, col = NG[i]
                    lr, lc, ld, lcol = LG[i]
                    ncol = col + mrounds * (col - lcol)
                    NG[i] = (r, c, d, ncol)

        else:
            seen = set()
            last_seen = n
            LG = NG.copy()

    seen.add(state)

    # if removed:
    #     print(f"{n=} {tcols=} ng={len(NG)}")
    G = NG
    n += 1
    if len(G) == 0:
        break


print(f"{n - 1}")
