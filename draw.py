#!/usr/bin/env python

import sys
from PIL import Image
import numpy as np


def mapv(v, s1, e1, s2, e2):
    return s2 + (e2 - s2) * ((v - s1) / (e1 - s1))


if __name__ == '__main__':
    if len(sys.argv) <= 1 or len(sys.argv[1]) <= 0:
        print('usage: ./draw.py out.png < out.txt')
        exit(1)

    filename = sys.argv[1]
    screen = []
    min_n, max_n = sys.maxsize, 0
    for line in sys.stdin:
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
    img.save(filename)
