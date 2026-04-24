# https://leetcode.com/problems/furthest-point-from-origin

def futhestDistanceFromOrigin(moves: str) -> int:

    dist = 0
    right = 0
    left = 0

    for move in moves:
        if move == 'L':
            dist -= 1
        elif move == 'R':
            dist += 1
        elif move == "_":
            left += 1
            right += 1

    return max(abs(dist - left), abs(dist + right))


moves = "L_RL__R"
print(futhestDistanceFromOrigin(moves))

moves = "_______"
print(futhestDistanceFromOrigin(moves))

moves = "_R__LL_"
print(futhestDistanceFromOrigin(moves))