#!/usr/bin/env pypy3

import fileinput


# counters
t = 0

P = {}
W = 100000
DIRS = [
    (1, 1),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 1),
    (0, 1),
]
G = []
R = 0
C = 0
F = 0
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    G.append(list(l))
    if l[0] != ".":
        F = R
    R += 1

C = len(G[0])
F = F % 2

round = 0
war = 0
while True:
    dr, dc = DIRS[round % len(DIRS)]
    round += 1
    sh = [0] * R

    step = 1
    if dr == 0:
        step = 2
    for c in range(0, C, step):
        if dc < 0:
            cc = C - 1 - c
        else:
            cc = c
        # check e
        for r in range(R):
            ccc = cc
            if dr == 0:
                off = (r + F) % 2
                ccc += dc * off
            if not (0 <= ccc < C):
                continue
            if G[r][ccc] not in ".xyz" and int(G[r][ccc]) > sh[r]:
                t += 1
                sh[r] = int(G[r][ccc])
                G[r][ccc] = str(1 + int(G[r][ccc]))
        # progress
        if dr == 1:
            nsh = [0]
            for r in range(R - 1):
                nsh.append(max(0, sh[r] - 1))
        elif dr == -1:
            nsh = []
            for r in range(1, R):
                nsh.append(max(0, sh[r] - 1))
            nsh.append(0)
        else:
            nsh = []
            for r in range(R):
                nsh.append(max(0, sh[r] - 1))

        sh = nsh
    for r in range(R):
        for c in range(C):
            if G[r][c] == "10":
                war += 1
                G[r][c] = "x"
            elif G[r][c] == "x":
                G[r][c] = "y"
            elif G[r][c] == "y":
                G[r][c] = "z"
            elif G[r][c] == "z":
                G[r][c] = "1"

    if war >= W:
        break
print(f"{t}")
