#!/usr/bin/python3
'''
An array of arrays, each entry is a box with a key to another. Box no is same
key no.as A solution that can efficiently determine if all boxes can be opened
'''

def canUnlockAll(boxes):
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
