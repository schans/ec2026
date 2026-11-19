#!/usr/bin/env pypy3

import fileinput

# counters
t = 0

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    lines.append(l.split())

for line in lines:
    s = []
    fin = False

    while not fin:
        fin = True
        for com in line:
            [l, c, r] = list(com)
            if c == "<":
                l, r = r, l

            if not len(s):
                s.append(l)
                s.append(r)
                continue

            if l in s and not r in s:
                s.insert(s.index(l) + 1, r)
                continue

            if r in s and not l in s:
                s.insert(s.index(r), l)
                continue

            if r not in s and not l in s:
                fin = False
                continue

            # both are in list
            ri = s.index(r)
            li = s.index(l)
            if li > ri:
                fin = False
                s[ri], s[li] = l, r

    t += int("".join(s))

print(f"{t}")
