# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square

from typing import List

import bisect
def maxDistnace(side: int, points: List[List[int]], k: int) -> int:
    answer = 0

    posarr = []
    for x, y in points:
        if x == 0:
            posarr.append(y)
        elif y == side:
            posarr.append(side + x)
        elif x == side:
            posarr.append(3 * side - y)
        else:
            posarr.append(4 * side - x)

    posarr.sort()
    perimiter = 4 * side
    def check(limit):
        for start in posarr:
            end = start + perimiter - limit
            curr = start

            for _ in range(k - 1):
                idx = bisect.bisect_left(posarr, curr+ limit)
                if idx == len(posarr) or posarr[idx] > end:
                    curr = -1
                    break
                curr = posarr[idx]
            if curr >= 0:
                return True
        return False
    
    left, right = 0, side

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

side = 2
points = [[0,0],[0,2],[2,0],[2,2]]
k = 4
print(maxDistnace(side, points, k))

side = 2
points = [[0,0], [1,2], [2,0], [2,2],[2,1]]
k = 4
print(maxDistnace(side, points, k))


side = 2
points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]]
k = 5
print(maxDistnace(side, points, k))