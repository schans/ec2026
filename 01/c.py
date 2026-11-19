#!/usr/bin/env pypy3

import fileinput

# counters
t = 0

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    lines.append(l)

n = lines[0].split(",")
N = len(n)

b = 3
b2 = b**2
c2 = 1

for m in n:
    c = int(m)
    while not (c <= (b2 - c2)):
        b += 2
        b2 = b**2
    t += b2 - c2 - c

print(f"{t}")
