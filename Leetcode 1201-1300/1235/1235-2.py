# Leetcode 1235: Maximum Profit in Job Scheduling
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# Solved on 27th of August, 2025
from bisect import bisect_right


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        """
        Calculates the maximum profit achievable by scheduling non-overlapping jobs.
        :param startTime: A list of integers representing the start times of jobs.
        :param endTime: A list of integers representing the end times of jobs.
        :param profit: A list of integers representing the profit of jobs.
        :return: The maximum profit that can be obtained.
        """
        # Create list of jobs and sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        # endTimes[i] = end time of job i (0-indexed in jobs)
        endTimes = [jobs[i][1] for i in range(n)]
        # dp[i] = max profit considering first i jobs (i from 0..n). dp[0] = 0 (no jobs)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            s, e, p = jobs[i - 1]
            # Find count of jobs with endTime <= s (they are 0..j-1). bisect_right returns that count
            j = bisect_right(endTimes, s)
            # If we include this job, profit = dp[j] + p (j may be 0 -> dp[0] = 0)
            include_profit = dp[j] + p
            # Exclude profit is dp[i-1] (skip current job)
            dp[i] = max(dp[i - 1], include_profit)

        return dp[n]