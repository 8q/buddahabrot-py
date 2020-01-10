#!/usr/bin/env python

from PIL import Image
import numpy as np


def mapv(v, s1, e1, s2, e2):
    return s2 + (e2 - s2) * ((v - s1) / (e1 - s1))


screen = []
min_n, max_n = 99999999, 0
for line in open('out.txt', 'r'):
    ls = []
    for s in line.split(','):
        n = int(s)
        min_n = n if n < min_n else min_n
        max_n = n if n > max_n else max_n
        ls.append(n)
    screen.append(ls)

H, W = len(screen), len(screen[0])

for y in range(H):
    for x in range(W):
        screen[y][x] = mapv(screen[y][x], min_n, max_n, 0, 255)

img = Image.fromarray(np.array(screen).astype(np.uint8))
img.save('out.jpg')
