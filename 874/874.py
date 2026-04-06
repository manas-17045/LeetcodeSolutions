# Leetcode 874: Walking Robot Simulation
# https://leetcode.com/problems/walking-robot-simulation/
# Solved on 6th of April, 2026
class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        """
        Simulates the movement of a robot on an infinite XY-plane based on commands and obstacles.

        :param commands: A list of integers where -2 means turn left, -1 means turn right, and 1-9 means move forward.
        :param obstacles: A list of [x, y] coordinates representing obstacles.
        :return: The maximum Euclidean distance squared from the origin that the robot reaches.
        """
        obstacleSet = {tuple(obs) for obs in obstacles}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        currentDir = 0
        currentX = 0
        currentY = 0
        maxDist = 0

        for cmd in commands:
            if cmd == -2:
                currentDir = (currentDir - 1) % 4
            elif cmd == -1:
                currentDir = (currentDir + 1) % 4
            else:
                for step in range(cmd):
                    nextX = currentX + directions[currentDir][0]
                    nextY = currentY + directions[currentDir][1]
                    if (nextX, nextY) in obstacleSet:
                        break

                    currentX = nextX
                    currentY = nextY

                maxDist = max(maxDist, currentX * currentX + currentY * currentY)

        return maxDist