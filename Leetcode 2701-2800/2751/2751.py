# Leetcode 2751: Robot Collisions
# https://leetcode.com/problems/robot-collisions/
# Solved on 3rd of November, 2025
class Solution:
    def survivedRobotHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        """
        Calculates the healths of robots that survive collisions.

        Robots move along a line, and when two robots collide, the one with
        lower health is destroyed. If healths are equal, both are destroyed.
        The surviving robot's health decreases by 1.

        Args:
            positions: A list of integers representing the initial positions of the robots.
            healths: A list of integers representing the initial healths of the robots.
            directions: A string where 'L' means moving left and 'R' means moving right.

        Returns:
            A list of integers representing the healths of the robots that survive,
            sorted by their original index.
        """
        numRobots = len(positions)
        indices = list(range(numRobots))

        indices.sort(key=lambda i: positions[i])

        stack = []

        for robotIndex in indices:
            if directions[robotIndex] == 'R':
                stack.append(robotIndex)
            else:
                while stack and healths[robotIndex] > 0:
                    rightRobotIndex = stack.pop()

                    if healths[robotIndex] > healths[rightRobotIndex]:
                        healths[robotIndex] -= 1
                        healths[rightRobotIndex] = 0
                    elif healths[robotIndex] < healths[rightRobotIndex]:
                        healths[robotIndex] = 0
                        healths[rightRobotIndex] -= 1
                        stack.append(rightRobotIndex)
                    else:
                        healths[robotIndex] = 0
                        healths[rightRobotIndex] = 0

        survivors = []
        for health in healths:
            if health > 0:
                survivors.append(health)

        return survivors