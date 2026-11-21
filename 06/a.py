#!/usr/bin/env pypy3

import fileinput

from collections import deque

# counters
t = 0

M = {}

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    i, ing = l.split(":")
    M[i] = ing.split(",")

print(M)

q = deque()
q.append("NULL")
SEEN = set()
while q:
    ing = q.popleft()
    if ing in SEEN:
        continue
    SEEN.add(ing)

    if ing in M:
        for si in M[ing]:
            q.append(si)


t = len(SEEN) - 1
print(f"{t}")
