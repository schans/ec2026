#!/usr/bin/env pypy3

import fileinput

from pprint import pprint
from copy import deepcopy

# counters
t = 0

IMP = 5
C = {}
IDS = set()
mc_nr = 0
mc_id = 0

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    # id=1, energy=5, connections=2,5,7

    parts = l.split(", ")

    id = parts[0].split("=")[1]
    en = int(parts[1].split("=")[1])
    co = parts[2].split("=")[1].split(",")

    C[id] = {"en": en, "co": co, "im": 0}
    IDS.add(id)
    print(f"{id=} {en=} {co=}")
    if len(co) > mc_nr:
        mc_nr = len(co)
        mc_id = id

print(f"{mc_id=} {mc_nr=}")
C[mc_id]["im"] = 1

strength = 4
while strength:
    print("Strength", strength)
    fired = set()
    imps = []
    for id in IDS:
        im = C[id]["im"]
        if im > 0:
            fired.add(id)
            for n in C[id]["co"]:
                imps.append((n, im))

    # if not fired:
    #     break

    for id in fired:
        C[id]["en"] += C[id]["im"] * (strength + 1)
        C[id]["im"] = 0

    print("imps", imps)
    for id, im in imps:
        C[id]["im"] += im
        # print("add imp", im, "to id", id)

    pprint(C)
    strength -= 1

for id in IDS:
    t += C[id]["en"] + C[id]["im"]
print(f"{t}")
