# Leetcode 2463: Minimum Total Distance Traveled
# https://leetcode.com/problems/minimum-total-distance-traveled/
# Solved on 14th of April, 2026
class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        """
        Calculates the minimum total distance traveled by all robots to reach a factory,
        given that each factory has a specific capacity limit.

        :param robot: A list of integers representing the positions of the robots.
        :param factory: A list of lists where each sublist [position, limit] represents
                        a factory's position and the maximum number of robots it can repair.
        :return: The minimum total distance traveled by all robots as an integer.
        """
        robot.sort()
        factory.sort()

        totalRobots = len(robot)
        minDistances = [float('inf')] * (totalRobots + 1)
        minDistances[0] = 0

        for factoryIndex in range(len(factory)):
            factoryPos, factoryLimit = factory[factoryIndex]

            for robotCount in range(totalRobots, 0, -1):
                currentDistanceSum = 0

                for assignedCount in range(1, min(robotCount, factoryLimit) + 1):
                    currentDistanceSum += abs(robot[robotCount - assignedCount] - factoryPos)

                    if minDistances[robotCount - assignedCount] != float('inf'):
                        newDistance = minDistances[robotCount - assignedCount] + currentDistanceSum
                        if newDistance < minDistances[robotCount]:
                            minDistances[robotCount] = newDistance

        return int(minDistances[totalRobots])