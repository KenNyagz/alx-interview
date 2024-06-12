#!/usr/bin/python3
'''
An array of arrays, each entry is a box with a key to another. Box no is same
key no.as A solution that can efficiently determine if all boxes can be opened
'''


def canUnlockAll(boxes, start=[]):
    ''' Iterative approach'''
    n = len(boxes)
    unlocked = [False] * n  # Track which boxes are unlocked
    stack = [start]  # Start with the initial box

    while stack:
        current = stack.pop()
        if not unlocked[current]:
            unlocked[current] = True  # Mark the current box as unlocked
            key = boxes[current]  # Get the key inside the current box
            if not unlocked[key]:  # If the box to which the key belongs is not unlocked
                stack.append(key)  # Add it to the stack

    return all(unlocked)
