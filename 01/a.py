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

b = 0
b2 = b**2
c2 = (b + 1) ** 2

for m in n:
    c = int(m)
    while not (b2 < c <= c2):
        b += 1
        b2 = b**2
        c2 = (b + 1) ** 2
    t += c2 - c

print(f"{t}")
