#!/usr/bin/env pypy3

import fileinput

from collections import defaultdict

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
    if limit == 1:
        return 1

    branches = defaultdict(int)
    t = 1
    total = 1
    branches[1] = 1
    while True:
        # advance
        longest = max(branches.keys())
        advance = growth - longest - 1
        if advance > 0:
            t += advance
            nb = defaultdict(int)
            for br_l, br_c in branches.items():
                nb[br_l + advance] = br_c
            branches = nb

        # grow + split
        br_t = 0
        nb = defaultdict(int)
        for br_l, br_c in branches.items():
            if br_l + 1 == growth:
                # split
                nb[growth // 2] += br_c * 2
                # new
                nb[1] += br_c
                total += br_c
                br_t += br_c * 3
            else:
                nb[br_l + 1] += br_c
                br_t += br_c

        branches = nb
        t += 1
        assert total == (br_t + 1) // 2
        if total >= limit:
            break

    # print(f"FINAL {t=} {growth=} {limit=} {total=}")
    return t


for grow, limit in L:
    t += calc(grow, limit)

print(f"{t}")
