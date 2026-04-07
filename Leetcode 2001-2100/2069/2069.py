# Leetcode 2069: Walking Robot Simulation II
# https://leetcode.com/problems/walking-robot-simulation-ii/
# Solved on 7th of MApril, 2026
class Robot:

    def __init__(self, width: int, height: int):
        self.gridWidth = width
        self.gridHeight = height
        self.perimeter = 2 * (width - 1) + 2 * (height - 1)
        self.currentPos = 0
        self.isStart = True

    def step(self, num: int) -> None:
        self.isStart = False
        self.currentPos = (self.currentPos + num) % self.perimeter

    def getPos(self) -> list[int]:
        if self.currentPos == 0:
            return [0, 0]
        elif self.currentPos < self.gridWidth:
            return [self.currentPos, 0]
        elif self.currentPos < self.gridWidth + self.gridHeight - 1:
            return [self.gridWidth - 1, self.currentPos - self.gridWidth + 1]
        elif self.currentPos < 2 * self.gridWidth + self.gridHeight - 2:
            return [2 * self.gridWidth + self.gridHeight - 3 - self.currentPos, self.gridHeight - 1]
        else:
            return [0, self.perimeter - self.currentPos]

    def getDir(self) -> str:
        if self.currentPos == 0:
            return "East" if self.isStart else "South"
        elif self.currentPos < self.gridWidth:
            return "East"
        elif self.currentPos < self.gridWidth + self.gridHeight - 1:
            return "North"
        elif self.currentPos < 2 * self.gridWidth + self.gridHeight - 2:
            return "West"
        else:
            return "South"