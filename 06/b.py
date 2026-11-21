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


SEEN = set()
q = deque()
for ing in M:
    if "NULL" in M[ing]:
        q.append(ing)

while q:
    ing = q.popleft()
    if ing in SEEN or ing == "NULL":
        continue
    SEEN.add(ing)

    for si in M:
        if ing in M[si]:
            q.append(si)


t = len(SEEN)
print(f"{t}")
