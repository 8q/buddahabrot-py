#!/usr/bin/env python

import numpy as np
from tqdm import tqdm
import multiprocessing as mp


H, W = 1000, 1000
MaxDepth = 1000
IterationsPerThread = 150000
Threads = 20000


def mapv(v, s1, e1, s2, e2):
    return s2 + (e2 - s2) * ((v - s1) / (e1 - s1))


def buddha_calc(a, b):
    c = complex(a, b)
    z = c
    ls = []
    for _ in range(MaxDepth):
        if abs(z) >= 2:
            return ls
        ls.append(z)
        z = z ** 2 + c
    return []


def paralell_task(_id):
    s = np.zeros((H, W), dtype=int)
    for _ in range(IterationsPerThread):
        h, w = np.random.rand() * H, np.random.rand() * W
        a, b = mapv(h, 0, H, -2, 2), mapv(w, 0, W, -2, 2)
        ls = buddha_calc(a, b)
        for c in ls:
            y, x = int(np.floor(mapv(c.imag, -2, 2, 0, H))
                       ), int(np.floor(mapv(c.real, -2, 2, 0, W)))
            s[y][x] = s[y][x] + 1
    return s


def buddhabrot_multi():
    worker_processes = max(mp.cpu_count() * 3 // 4, 1)
    p = mp.Pool(worker_processes)
    screen = np.zeros((H, W), dtype=int)
    with tqdm(total=Threads) as t:
        for res in p.imap_unordered(paralell_task, [i for i in range(Threads)]):
            screen = np.add(screen, res)
            t.update()
    return screen


if __name__ == '__main__':
    screen = buddhabrot_multi().tolist()
    for line in screen:
        print(','.join(map(str, line)))
