# https://leetcode.com/problems/furthest-point-from-origin

from collections import Counter


def futhestDistanceFromOrigin(moves: str) -> int:

    d, l, r, u = 0, 0, 0, 0

    for move in moves:
        if move == 'L':
            d -= 1
            l += 1
        elif move == 'R':
            d += 1
            r += 1
        elif move == "_":
            u +=1

    return abs(d - u) if l > r else abs(d + u)

moves = "L_RL__R"
print(futhestDistanceFromOrigin(moves))

moves = "_______"
print(futhestDistanceFromOrigin(moves))

moves = "_R__LL_"
print(futhestDistanceFromOrigin(moves))

moves = "L_L__R"
print(futhestDistanceFromOrigin(moves))