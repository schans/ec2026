#!/usr/bin/env pypy3

import fileinput


# counters
t = 0

P = {}

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    # id=1 quest=1 part=1 time=187
    e = []
    parts = line.split()
    assert len(parts) == 4
    for p in parts:
        _, v = p.split("=")
        e.append(int(v))
    lines.append(e)
    if e[0] in P:
        P[e[0]] = (-1 + P[e[0]][0], int(e[3]) + P[e[0]][1])
    else:
        P[e[0]] = (1000, int(e[3]))

i = 1
for v in sorted(set(P.values())):
    t += v[1] * i
    i += 1

print(f"{t}")
