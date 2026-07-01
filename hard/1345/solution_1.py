# https://leetcode.com/problems/jump-game-iv

from typing import List
from collections import defaultdict, deque

def minJumps(arr: List[int]) -> int:
    n = len(arr)
    if n == 1:
        return 0

    # Build value -> indices map for same-value jumps
    value_to_indices = defaultdict(list)
    for i, v in enumerate(arr):
        value_to_indices[v].append(i)

    visited = {0}
    queue = deque([(0, 0)])  # (index, steps)

    while queue:
        idx, steps = queue.popleft()

        # Candidates: adjacent indices + all same-value indices
        candidates = [idx - 1, idx + 1] + value_to_indices[arr[idx]]

        # Delete after use so we never re-enqueue this same-value group
        del value_to_indices[arr[idx]]

        for nxt in candidates:
            if nxt == n - 1:
                return steps + 1
            if 0 <= nxt < n and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, steps + 1))

    return -1


arr = [100,-23,-23,404,100,23,23,23,3,404]

print(minJumps(arr))