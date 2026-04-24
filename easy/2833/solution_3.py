# https://leetcode.com/problems/furthest-point-from-origin

from collections import Counter


def futhestDistanceFromOrigin(moves: str) -> int:
    dc = Counter(moves)

    d, l, r, u = dc.get('R', 0) - dc.get('L', 0), dc.get('L', 0), dc.get('R', 0), dc.get('_', 0)

    return abs(d - u) if l > r else abs(d + u)

moves = "L_RL__R"
print(futhestDistanceFromOrigin(moves))

moves = "_______"
print(futhestDistanceFromOrigin(moves))

moves = "_R__LL_"
print(futhestDistanceFromOrigin(moves))

moves = "L_L__R"
print(futhestDistanceFromOrigin(moves))