#!/usr/bin/env python
# coding=utf-8


# aseq = "abcd"
aseq = [1, 2, 3, 4]

print(type(aseq))

print(aseq + aseq)

print(aseq * 4)

print(aseq[0])

print(type(aseq[0]))

print(aseq[-2])

print(aseq[1:-2])

print(aseq[1:2])

# bseq = "abdc"
bseq = [1, 3, 2, 4]

print(aseq < bseq)

for elem in aseq:
    print(elem)

print(min(aseq))

print(max(aseq))

print(sorted(aseq))
