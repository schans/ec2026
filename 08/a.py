#!/usr/bin/env pypy3

import fileinput


# counters
t = 0

P = {}

G = []
R = 0
C = 0
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    G.append(list(l))
    R += 1

C = len(G[0])

sh = [0] * R
for c in range(C):
    # check e
    for r in range(R):
        if G[r][c] != "." and int(G[r][c]) > sh[r]:
            t += 1
            sh[r] = int(G[r][c])
    # progress
    nsh = [0]
    for r in range(R - 1):
        nsh.append(sh[r] - 1)
    sh = nsh

print(f"{t}")
