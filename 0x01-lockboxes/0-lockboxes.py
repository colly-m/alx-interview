#!/usr/bin/python3
"""Method to determine if boxes can be opened or not"""
from collections import deque


def canUnlockAll(boxes):
    """Checking which boxes can be opened then return true or false"""
    if not boxes:
        return False

    n_boxes = len(boxes)
    visited = [False] * n_boxes
    visited[0] = True
    queue = deque([0])

    while queue:
        curr_box = queue.popleft()

        for key in boxes[curr_box]:
            if 0 <= key < n_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
