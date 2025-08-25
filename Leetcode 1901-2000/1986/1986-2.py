# Leetcode 1986: Minimum Number of Work Sessions to Finish the Tasks
# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
# Solved on 25th of August, 2025
class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        """
        Calculates the minimum number of sessions required to complete all tasks.
        :param tasks: A list of integers representing the time required for each task.
        :param sessionTime: An integer representing the maximum time allowed for a single session.
        :return: An integer representing the minimum number of sessions needed.
        """
        n = len(tasks)
        full = (1 << n) - 1
        INF = 10**9

        dp: list[tuple[int, int]] = [(INF, 0)] * (1 << n)
        dp[0] = (1, 0)

        for mask in range(1, 1 << n):
            best_sessions, best_last_time = INF, 0
            # Try finishing mask by placing task j last
            m = mask
            j = 0
            while m:
                if m & 1:
                    prev_mask = mask ^ (1 << j)
                    prev_sessions, prev_time = dp[prev_mask]
                    # Try to put tasks[j] into the last session if possible
                    if prev_time + tasks[j] <= sessionTime:
                        cand = (prev_sessions, prev_time + tasks[j])
                    else:
                        # Need a new session for tasks[j]
                        cand = (prev_sessions + 1, tasks[j])

                    # Choose lexicographically smaller: fewer sessions first, then smaller last_time
                    if cand[0] < best_sessions or (cand[0] == best_sessions and cand[1] < best_last_time):
                        best_sessions, best_last_time = cand

                m >>= 1
                j += 1

            dp[mask] = (best_sessions, best_last_time)

        return dp[full][0]