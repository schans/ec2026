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
    for x in range(S):
        t += int(b[x]) ** (S - x - 1) * int(n[x])

print(f"{t}")
