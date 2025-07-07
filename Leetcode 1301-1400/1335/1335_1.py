# Leetcode 1335: Minimum Difficulty of a Job Schedule
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
# Solved on 7th of July, 2025
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        """
        Calculates the minimum difficulty of a job schedule.

        Given an array of integers `jobDifficulty` representing the difficulty of each job
        and an integer `d` representing the number of days, the goal is to schedule
        all jobs over `d` days. On each day, you must complete at least one job.
        The difficulty of a day is the maximum difficulty of any job completed on that day.
        The total difficulty of the schedule is the sum of the difficulties of each day.

        Args:
            jobDifficulty: A list of integers representing the difficulty of each job.
            d: The number of days to schedule the jobs.
        """
        jobCount = len(jobDifficulty)
        if jobCount < d:
            return -1

        memo = {}

        def solve(jobIndex, daysLeft):
            state = (jobIndex, daysLeft)
            if state in memo:
                return memo[state]

            if daysLeft == 1:
                return max(jobDifficulty[jobIndex:])

            res = float('inf')
            maxDifficultyToday = 0

            lastJobTodayIndexLimit = jobCount - daysLeft
            for i in range(jobIndex, lastJobTodayIndexLimit + 1):
                maxDifficultyToday = max(maxDifficultyToday, jobDifficulty[i])
                difficultyOfRest = solve((i + 1), (daysLeft - 1))
                res = min(res, (maxDifficultyToday + difficultyOfRest))

            memo[state] = res
            return res

        return solve(0, d)