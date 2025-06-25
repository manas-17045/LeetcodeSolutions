# Leetcode 2398: Maximum Number of Robots Within Budget
# https://leetcode.com/problems/maximum-number-of-robots-within-budget/
# Solved on 25th of June, 2025
from collections import deque


class Solution:
    def maximumRobots(self, chargeTimes: list[int], runningCosts: list[int], budget: int) -> int:
        """
        Finds the maximum number of robots that can be run simultaneously within a given budget.

        The cost of running k robots is calculated as:
        max(chargeTimes[i] for i in the chosen k robots) + k * sum(runningCosts[i] for i in the chosen k robots).

        Args:
            chargeTimes: A list of integers representing the charge time for each robot.
            runningCosts: A list of integers representing the running cost for each robot.
            budget: An integer representing the maximum allowed budget.

        Returns:
            An integer representing the maximum number of robots that can be run simultaneously.
        """
        maxDq = deque()     # will store indices of chargeTimes in decreasing order
        sum_run = 0
        i = 0
        best = 0

        for j, (r, c) in enumerate(zip(chargeTimes, runningCosts)):
            # Add new robot j
            sum_run += r
            # Maintain deque so that chargeTimes[maxDq[0]] is max in window
            while maxDq and chargeTimes[maxDq[-1]] <= c:
                maxDq.pop()
            maxDq.append(j)

            # Shrink from left while over budget
            while maxDq and (chargeTimes[maxDq[0]] + (j - i + 1) * sum_run) > budget:
                # If the max is going out, of window, pop it.
                if maxDq[0] == i:
                    maxDq.popleft()
                # Remove robot i
                sum_run -= runningCosts[i]
                i += 1

            # Update best window length
            best = max(best, (j - i + 1))

        return best