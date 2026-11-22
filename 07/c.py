#!/usr/bin/env pypy3

import fileinput

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

    C[id] = {"en": en, "co": co}
    IDS.add(id)
    # print(f"{id=} {en=} {co=}")
    if len(co) > mc_nr:
        mc_nr = len(co)
        mc_id = id


# print(f"{mc_id=} {mc_nr=}")


def reduced_im(imps):
    ni = []
    S = set()
    for id, im, st in imps:
        if (id, st) in S:
            nni = []
            for nid, nim, nst in ni:
                if id == nid and st == nst:
                    nni.append((nid, im + nim, st))
                else:
                    nni.append((nid, nim, nst))
            ni = nni
        else:
            S.add((id, st))
            ni.append((id, im, st))
    return ni


EXPL = 1000000
sums = []
O_IDS = IDS
O_C = C
for id in O_IDS:
    imps = [(id, 1, 10)]
    round = 1
    IDS = O_IDS.copy()
    C = deepcopy(O_C)

    while True:
        # print()
        # print(f"Stage {round}:")
        round += 1
        fired = set()

        # print("imps", imps)

        new_imps = []
        for id, im, st in imps:
            if id not in IDS:
                continue
            # print(
            #     f"cloud {id} received {im} impulses with strength {st}: +{st * im} (energy {C[id]['en']} -> {C[id]['en'] + st * im})"
            # )
            C[id]["en"] += im * st
            if st > 1:
                for n in C[id]["co"]:
                    new_imps.append((n, im, st - 1))

        exploded = []
        # print("Explosions after this stage:")
        for id in IDS:
            if C[id]["en"] >= EXPL:
                # print("cloud", id, "exploded at energy", C[id]["en"])
                exploded.append(id)
                for co in C[id]["co"]:
                    if co in IDS:
                        # print(
                        #     "  new impulse with strength 10: cloud", id, "-> cloud", co
                        # )
                        new_imps.append((co, 1, 10))

        for id in exploded:
            del C[id]
            IDS.remove(id)
            for n in IDS:
                if id in C[n]["co"]:
                    C[n]["co"].remove(id)

        if not new_imps:
            break
        imps = reduced_im(new_imps)

    t = 0
    for id in IDS:
        t += C[id]["en"]
    sums.append(t)

print(f"{max(sums)}")
