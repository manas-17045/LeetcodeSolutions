# Leetcode 1986: Minimum Number of Work Sessions to Finish the Tasks
# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/
# Solved on 25th of August, 2025
class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        """
        Calculates the minimum number of work sessions required to complete all tasks.

        Args:
            tasks: A list of integers representing the time required for each task.
            sessionTime: An integer representing the maximum time available for each session.

        Returns:
            An integer representing the minimum number of work sessions.
        """
        numTasks = len(tasks)
        numMasks = 1 << numTasks

        # Initialize DP with a value larger than ny possible result.
        dp = [(numTasks + 1, 0)] * numMasks

        dp[0] = (0, sessionTime + 1)

        for mask in range(numMasks):
            if dp[mask][0] > numTasks:
                continue

            numSessions, usedTime = dp[mask]

            for i in range(numTasks):
                if not ((mask >> i) & 1):
                    newMask = mask | (1 << i)
                    currentTaskTime = tasks[i]

                    # Add the task to the current session if it fits.
                    if usedTime + currentTaskTime <= sessionTime:
                        candidateState = (numSessions, usedTime + currentTaskTime)
                        if candidateState < dp[newMask]:
                            dp[newMask] = candidateState

                    # Start a new session for this task.
                    else:
                        candidateState = (numSessions + 1, currentTaskTime)
                        if candidateState < dp[newMask]:
                            dp[newMask] = candidateState

        return dp[numMasks - 1][0]