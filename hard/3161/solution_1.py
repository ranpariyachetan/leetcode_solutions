# https://leetcode.com/problems/block-placement-queries

from typing import List
import bisect


def getResults(queries: List[List[int]]) -> List[bool]:    
    bit, answer = [0] * (min(50000, 3 * len(queries)) + 1), []

    def bit_range(p, down=True):
        while p >= 0 and p < len(bit):
            yield p
            p = (p & (p + 1)) - 1 if down else p | (p + 1)

    def get_max(p: int) -> int:
        return max(bit[i] for i in bit_range(p))
    
    def update(p: int, v: int):
        for i in bit_range(p, False):
            bit[i] = max(bit[i], v)

    blocks = [0] + sorted(x for t, x, *sz in queries if t == 1)

    for i, b in enumerate(blocks[1:]):
        update(b, b - blocks[i])

    for t, x, *sz in reversed(queries):
        p = bisect.bisect_left(blocks, x)
        if t == 1:
            if p + 1 < len(blocks):
                update(blocks[p + 1], blocks[p + 1] - blocks[p - 1])
            del blocks[p]
        else:
            answer.append(x - blocks[p - 1] >= sz[0] or get_max(x) >= sz[0])

    return list(reversed(answer))

# Test cases
queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
print(getResults(queries))

queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
print(getResults(queries))

queries = [[1,4],[2,1,2]]
print(getResults(queries))

queries = [[1,1],[1,5],[1,13],[1,14],[2,12,8]]
print(getResults(queries))

queries = [[2,1,1]]
print(getResults(queries))