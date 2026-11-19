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
        P[e[0]] += int(e[3])
    else:
        P[e[0]] = int(e[3])

i = 1
for k, v in sorted(P.items(), key=lambda item: item[1]):
    t += v * i
    i += 1

print(f"{t}")
