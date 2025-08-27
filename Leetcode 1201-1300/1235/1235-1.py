# Leetcode 1235: Maximum Profit in Job Scheduling
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# Solved on 27th of August, 2025
import bisect


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        """
        Calculates the maximum profit that can be obtained by scheduling jobs.

        Args:
            startTime: A list of integers representing the start times of the jobs.
            endTime: A list of integers representing the end times of the jobs.
            profit: A list of integers representing the profit of each job.

        Returns:
            The maximum profit that can be obtained.
        """
        numJobs = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda item: item[1])

        dp = [0] * numJobs
        dp[0] = jobs[0][2]

        endTimes = [job[1] for job in jobs]

        for i in range(1, numJobs):
            currentStart = jobs[i][0]
            currentProfit = jobs[i][2]

            prevJobIndex = bisect.bisect_right(endTimes, currentStart, hi=i) - 1

            profitWithCurrent = currentProfit
            if prevJobIndex >= 0:
                profitWithCurrent += dp[prevJobIndex]

            profitWithoutCurrent = dp[i - 1]

            dp[i] = max(profitWithCurrent, profitWithoutCurrent)

        return dp[-1]