#!/usr/bin/env pypy3

import fileinput

# counters
t = 0

P = {}
S = {}

Q = 0

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    # id=1 quest=1 part=1 time=187
    e = []
    parts = line.split()
    assert len(parts) == 4
    for p in parts:
        _, v = p.split("=")
        e.append(int(v))
    lines.append(e)
    Q = max(Q, int(e[1]))


def score(part):
    m = part * 50
    ps = 0
    pt = -1
    for k, v in sorted(P.items(), key=lambda item: item[1]):
        if v == pt:
            s = ps
        else:
            s = m
            ps = m

        # print(f"id={k}, time={v}, points={s}")
        if k in S:
            S[k] += max(0, s)
        else:
            S[k] = max(0, s)
        pt = v
        ps = s
        m -= 1


for quest in range(1, Q + 1):
    parts = 0
    for e in lines:
        if e[1] == quest:
            parts = max(parts, e[2])

    P = {}
    PO = {}
    for part in range(1, parts + 1):
        # print(f"{quest=} {part=}")
        for e in lines:
            if e[1] == quest and e[2] == part:
                if e[0] in P:
                    P[e[0]] += int(e[3])
                else:
                    P[e[0]] = int(e[3])
                    if e[0] in PO:
                        P[e[0]] += PO[e[0]]

        # print(P)
        score(part)
        PO = P
        P = {}


m = 1
pm = 0
pt = 0
t = 0
for k, v in sorted(S.items(), key=lambda item: -item[1]):
    if v == pt:
        r = pm
    else:
        r = m
        pt = v
        pm = m
    # print(f"{r}. points={v}")
    t += r * v
    m += 1
print(f"{t}")
