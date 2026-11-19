#!/usr/bin/env pypy3

import fileinput

# counters
t = 0

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    lines.append(l[4:].split())

S = len(lines[0][0])
for b, n in lines:
    S = len(n) - 1
    R = len(b)
    for x in range(S + 1):
        t += (int(b[(R - x - 1) % R]) ** x) * int(n[S - x])

print(f"{t}")
