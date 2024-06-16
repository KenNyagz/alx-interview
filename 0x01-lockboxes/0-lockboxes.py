#!/usr/bin/python3
'''
An array of arrays, each entry is a box with a key to another. Box no is same
key no.as A solution that can efficiently determine if all boxes can be opened
'''


def join(T, R):
    res = []
    for e in R:
        res += T[e]
    return res


def canUnlockAll(boxes):
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True
    # print(total)

    return len(total) == len(boxes)
