#!/usr/bin/env pypy3

import fileinput
from functools import cache


# counters
t = 0

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    lines.append(l[5:].split())


@cache
def iso(b: str, n: str) -> int:
    st = 0
    S = len(n) - 1
    R = len(b)
    for x in range(S + 1):
        st += (int(b[(R - x - 1) % R]) ** x) * int(n[S - x])
    return st


S = len(lines[0][0])
for b, n in lines:
    st = iso(b, n)
    for k in range(int(n) - 1, 0, -1):
        if st == iso(b, str(k)):
            st = 0
            break
    t += st


print(f"{t}")
