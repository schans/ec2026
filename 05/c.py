#!/usr/bin/env pypy3

import fileinput


# counters
t = 0

DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
D = set()
L = set()
S = set()
T = set()
R = 0
C = 0

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    C = len(l)

    for cc, c in enumerate(l.strip()):
        if c == "1":
            D.add((R, cc))

    R += 1

L.add((R // 2, C // 2))
NL = L.copy()


def dump():
    print("-" * C)
    for r in range(R):
        for c in range(C):
            if (r, c) in T:
                print("@", end="")
            elif (r, c) in S:
                print("=", end="")
            elif (r, c) in L:
                print("#", end="")
            elif (r, c) in D:
                print(".", end="")
            else:
                print(".", end="")
        print()
    print("-" * C)


# land
done = False
while not done:
    done = True
    for rr, cc in L:
        for dr, dc in DIRS:
            nr = rr + dr
            nc = cc + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in L:
                n = 0
                for ddr, ddc in DIRS:
                    r = nr + ddr
                    c = nc + ddc
                    if (r, c) in L or (r, c) in D:
                        n += 1
                    if n >= 5:
                        NL.add((nr, nc))
                        done = False
                        continue
    L = NL.copy()

# sand
done = False
NS = S.copy()
while not done:
    done = True
    for rr, cc in L:
        if (rr, cc) in S:
            continue

        for ddr, ddc in DIRS:
            r = rr + ddr
            c = cc + ddc
            if (r, c) not in L:
                NS.add((rr, cc))
                done = False

    S = NS.copy()

done = False
while not done:
    done = True
    for rr, cc in L:
        for dr, dc in DIRS:
            nr = rr + dr
            nc = cc + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in S:
                n = 0
                for ddr, ddc in DIRS:
                    r = nr + ddr
                    c = nc + ddc
                    if (r, c) in S:
                        n += 1
                    if n >= 5:
                        NS.add((nr, nc))
                        done = False
                        continue
    S = NS.copy()

# trees
TDIRS = []
for dr in [-2, -1, 0, 1, 2]:
    for dc in [-2, -1, 0, 1, 2]:
        TDIRS.append((dr, dc))
TDIRS.remove((-2, -2))
TDIRS.remove((-2, 2))
TDIRS.remove((2, -2))
TDIRS.remove((2, 2))

done = False
NT = T.copy()
while not done:
    done = True
    for rr, cc in L:
        if (rr, cc) in S or (rr, cc) in T:
            continue

        nt = True
        for ddr, ddc in TDIRS:
            r = rr + ddr
            c = cc + ddc
            if (r, c) not in L and (r, c) not in T or (r, c) in S:
                nt = False
                break

        if nt:
            NT.add((rr, cc))
            done = False

    T = NT.copy()

# grow
for _ in range(2):
    for rr, cc in L:
        if (rr, cc) in S or (rr, cc) in T:
            continue

        nt = 0
        hs = False
        for ddr, ddc in DIRS:
            r = rr + ddr
            c = cc + ddc
            if (r, c) in S:
                hs = True
            if (r, c) in T:
                nt += 1

        if not hs and nt >= 4:
            NT.add((rr, cc))
    T = NT.copy()

t = len(T)
print(f"{t}")
