# https://leetcode.com/problems/destroying-asteroids
from typing import List

def asteroidsDestroyed(mass: int, asteroids: List[int]) -> bool:
    asteroids.sort()
    for a in asteroids:
        if mass < a:
            return False
        mass += a
    return True

# Test cases
mass = 10
asteroids = [3,9,19,5,21]
print(asteroidsDestroyed(mass, asteroids))

mass = 5
asteroids = [4,9,23,4]
print(asteroidsDestroyed(mass, asteroids))