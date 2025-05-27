# Leetcode 2589: Minimum Time to Complete All Tasks
# https://leetcode.com/problems/minimum-time-to-complete-all-tasks/
# Solved on 27th of May, 2025

class Solution:
    def findMinimumTime(self, tasks: list[list[int]]) -> int:
        """
        Finds the minimum total time required to run all tasks.

        Each task is represented as [start, end, duration], meaning it must run
        for 'duration' seconds within the time interval [start, end].

        Args:
            tasks: A list of tasks, where each task is [start, end, duration].
        Returns:
            The minimum total time required to run all tasks.
        """
        # Find the maximum time we need to consider
        max_t = max(end for _, end, _ in tasks)
        # Boolean array: used[t] == 1 if second t is scheduled
        used = [0] * (max_t + 1)
        total_on = 0

        # Sort tasks by their end-time (earliest deadline first)
        tasks.sort(key=lambda x: x[1])

        for start, end, duration in tasks:
            # Count how many seconds are already scheduled in [start...end]
            already = 0
            for t in range(start, end + 1):
                already += used[t]

            need = duration - already
            if need <= 0:
                continue

            # Greedily fill 'need' free seconds from the back of the interval
            t = end
            while need > 0:
                if not used[t]:
                    used[t] = 1
                    total_on += 1
                    need -= 1
                t -= 1

        return total_on