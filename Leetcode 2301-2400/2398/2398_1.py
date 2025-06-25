# Leetcode 2398: Maximum Number of Robots Within Budget
# https://leetcode.com/problems/maximum-number-of-robots-within-budget/
# Solved on 25th of June, 2025
import collections


class Solution:
    def maximumRobots(self, chargeTimes: list[int], runningCosts: list[int], budget: int) -> int:
        """
        Finds the maximum number of consecutive robots that can be activated within a given budget.

        The cost of activating `k` robots is calculated as:
        `max(chargeTimes[i] for i in activated_robots) + k * sum(runningCosts[i] for i in activated_robots)`

        Args:
            chargeTimes: A list of integers representing the charge time of each robot.
            runningCosts: A list of integers representing the running cost of each robot.
            budget: An integer representing the maximum budget.
        """
        n = len(chargeTimes)
        left = 0
        maxNumRobots = 0
        windowRunningSum = 0
        windowChargeIndices = collections.deque()

        for right in range(n):
            windowRunningSum += runningCosts[right]

            while windowChargeIndices and chargeTimes[windowChargeIndices[-1]] <= chargeTimes[right]:
                windowChargeIndices.pop()
            windowChargeIndices.append(right)

            while windowChargeIndices:
                currentK = right - left + 1

                maxChargeInWindow = chargeTimes[windowChargeIndices[0]]
                cost = maxChargeInWindow + (currentK * windowRunningSum)

                if cost <= budget:
                    break
                else:
                    if windowChargeIndices[0] == left:
                        windowChargeIndices.popleft()

                    windowRunningSum -= runningCosts[left]
                    left += 1

            if left <= right:
                currentK = right - left + 1
                maxNumRobots = max(maxNumRobots, currentK)

        return maxNumRobots