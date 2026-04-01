# https://leetcode.com/problems/robot-collisions

from git import List

def survivedRobotsHealths(positions:List[int], healths: List[int], directions: str) -> List[int]:
    n = len(positions)
    robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(n)])
    stack = []
    survived = [True] * n

    for pos, health, direction, idx in robots:
        if direction == 'R':
            stack.append((health, idx))
        else:
            while stack:
                top_health, top_idx = stack[-1]
                if top_health < health:
                    survived[top_idx] = False
                    stack.pop()
                    healths[idx] -= 1
                    health -= 1
                elif top_health > health:
                    survived[idx] = False
                    stack[-1] = (top_health - 1, top_idx)
                    healths[top_idx] -= 1
                    health -= 1
                    break
                else:
                    survived[top_idx] = False
                    survived[idx] = False
                    stack.pop()
                    break

    return [healths[i] for i in range(n) if survived[i]]


positions = [5,4,3,2,1]
healths = [2,17,9,15,10]
directions = "RRRRR"

print(survivedRobotsHealths(positions, healths, directions))

positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"

print(survivedRobotsHealths(positions, healths, directions))

positions = [3,2,30,24,38,7]
healths = [47,12,49,11,47,38]
directions = "RRLRRR"
print(survivedRobotsHealths(positions, healths, directions))