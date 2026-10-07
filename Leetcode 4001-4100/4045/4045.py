# Leetcode 4045: Count Robot Groups
# https://leetcode.com/problems/count-robot-groups/
# Solved on 7th of October, 2026
class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        """
        Calculates the number of robot groups remaining after all possible merges.

        Parameters:
            position (list[int]): Strictly increasing initial positions of the robots.
            speed (list[int]): Constant speeds of the robots.
            distance (int): Distance threshold for robots to merge into a single group.

        Returns:
            int: Total number of robot groups remaining after all merges have occurred.
        """
        numRobots = len(position)
        groupCount = 1
        targetSpeed = speed[numRobots - 1]

        for currentIndex in range(numRobots - 2, -1, -1):
            if position[currentIndex + 1] - position[currentIndex] > distance:
                if speed[currentIndex] <= targetSpeed:
                    groupCount += 1
                    targetSpeed = speed[currentIndex]

        return groupCount