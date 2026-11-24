#!/usr/bin/env pypy3

import fileinput


# counters
t = 0

L = []

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    # id=1 quest=1 part=1 time=187
    e = []
    parts = l.split(", ")
    assert len(parts) == 3
    for p in parts[1:]:
        _, v = p.split("=")
        e.append(int(v))
    L.append(e)


def calc(growth: int, limit: int):
    t = 1
    branches = [1]
    knots = 0

    total = sum(branches) + knots
    while True:
        t += 1
        # grow
        for i in range(len(branches)):
            branches[i] += 1

        # split
        nb = []
        for br in branches:
            if not br % growth:
                # split
                nb.append(br // 2)
                nb.append(br // 2)
                # new
                nb.append(1)
                knots += 1
            else:
                nb.append(br)

        branches = nb
        total = sum(branches) + knots
        if total >= limit:
            break

    return t


for grow, limit in L:
    t += calc(grow, limit)

print(f"{t}")
