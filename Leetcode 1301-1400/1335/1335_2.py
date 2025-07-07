# Leetcode 1335: Minimum Difficulty of a Job Schedule
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
# Solved on 7th of July, 2025
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        """
        Calculates the minimum difficulty to complete all jobs within 'd' days.

        Args:
            jobDifficulty (list[int]): A list of integers representing the difficulty of each job.
            d (int): The number of days available to complete the jobs.

        Returns:
            int: The minimum difficulty to complete all jobs, or -1 if it's impossible
                 (i.e., if the number of jobs is less than the number of days).
        """
        n = len(jobDifficulty)
        if n < d:
            return -1

        INF = float('inf')
        dp = [[INF] * n for _ in range(d + 1)]

        maxd = 0
        for i in range(n):
            maxd = max(maxd, jobDifficulty[i])
            dp[1][i] = maxd

        for day in range(2, d + 1):
            for i in range(day - 1, n):
                max_seg = 0
                best = INF
                for j in range(i, day - 2, -1):
                    max_seg = max(max_seg, jobDifficulty[j])
                    prev = dp[day - 1][j - 1]
                    if prev + max_seg < best:
                        best = prev + max_seg
                dp[day][i] = best

        res = dp[d][n - 1]
        return res if res < INF else -1