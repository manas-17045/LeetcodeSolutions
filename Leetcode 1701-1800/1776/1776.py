# Leetcode 1776: Car Fleet II
# https://leetcode.com/problems/car-fleet-ii/
# Solved on 21st of October, 2025
class Solution:
    def getCollisionTimes(self, cars: list[list[int]]) -> list[float]:

        n = len(cars)
        collisionTimes = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            posI, speedI = cars[i]

            while stack:
                j = stack[-1]
                posJ, speedJ = cars[j]
                timeJ = collisionTimes[j]

                if speedI <= speedJ:
                    stack.pop()
                else:
                    catchUpTime = (posJ - posI) / (speedI - speedJ)

                    if timeJ != -1.0 and catchUpTime > timeJ:
                        stack.pop()
                    else:
                        collisionTimes[i] = catchUpTime
                        break

            stack.append(i)

        return collisionTimes