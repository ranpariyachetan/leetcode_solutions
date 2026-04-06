# https://leetcode.com/problems/robot-return-to-origin

import emoji

def judgeCircle(moves: str) -> bool:
    pos = [0, 0]

    directions = {"L": [-1, 0], "R": [1, 0], "U": [0, 1], "D": [0, -1]}

    for move in moves:
        pos[0] += directions[move][0]
        pos[1] += directions[move][1]

    return pos[0] == 0 and pos[1] == 0

def print_test_result(input, expected, actual):
    print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

moves = "UD"
print_test_result(moves, True, judgeCircle(moves))

moves = "LL"
print_test_result(moves, False, judgeCircle(moves))