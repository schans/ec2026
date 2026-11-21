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

S = {}

for nls in ["NULLv1", "NULLv2", "NULLv3"]:
    SEEN = set()
    q = deque()
    for ing in M:
        if nls in M[ing]:
            q.append(ing)

    while q:
        ing = q.popleft()
        if ing in SEEN or ing == nls:
            continue
        SEEN.add(ing)

        for si in M:
            if ing in M[si]:
                q.append(si)

    S[nls] = SEEN
    # print(SEEN)


t = len(
    (S["NULLv1"] & S["NULLv2"])
    | (S["NULLv1"] & S["NULLv3"])
    | (S["NULLv2"] & S["NULLv3"])
)

print(f"{t}")
