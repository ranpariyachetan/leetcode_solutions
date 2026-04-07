# https://leetcode.com/problems/walking-robot-simulation-ii

from typing import List
class Robot:

    next_dir = {"East": "North", "North":"West", "West": "South", "South": "East"}
    next_pos = {"East": [1, 0], "North":[0, 1], "West": [-1, 0], "South": [0, -1]}
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.curr_dir = "East"
        self.curr_pos = [0, 0]

    def step(self, num: int) -> None:
        target = num
        next_pos = self._getNextPos(num)
        while target > 0:
            isvalid, valid_pos = self._isValid(next_pos)
            if isvalid:
                self.curr_pos = next_pos
                target = 0
            else:
                self.curr_pos = valid_pos
                self.curr_dir = Robot.next_dir[self.curr_dir]
                next_pos = self._getNextPos()
                if self._isValid(next_pos):
                    self.curr_pos = next_pos

    def _isValid(self, pos):
        isvalid = pos[0] >= 0 and pos[0] < self.width and pos[1] >= 0 and pos[1] < self.height
        if not isvalid:
            return isvalid, [pos[0] - self.width, pos[1] - self.height]
        return isvalid, None
    
    def _getNextPos(self, distance):
        next_pos = [self.curr_pos[0] + Robot.next_pos[self.curr_dir][0] * distance, self.curr_pos[1] + Robot.next_pos[self.curr_dir][1] * distance]
        return next_pos

    def getPos(self) -> List[int]:
        return self.curr_pos

    def getDir(self) -> str:
        return self.curr_dir


# robot = Robot(6, 3)
# robot.step(2)
# robot.step(2)
# print(robot.getPos())  # expected = [4, 0]
# print(robot.getDir())  # expected = "E"
# robot.step(2)
# robot.step(1)
# robot.step(4)
# print(robot.getPos())  # expected = [1, 2]
# print(robot.getDir())  # expected = "W"
# # Your Robot object will be instantiated and called as such:
# # obj = Robot(width, height)
# # obj.step(num)
# # param_2 = obj.getPos()
# # param_3 = obj.getDir()

robot = Robot(19, 14)
robot.step(4602)
print(robot.getPos())  # expected = [18, 13]