# Leetcode 3376: Minimum Time to Break Locks I
# https://leetcode.com/problems/minimum-time-to-break-locks-i/
# Solved on 28th of November, 2025
class Solution:
    def findMinimumTime(self, strength: list[int], k: int) -> int:
        """
        Calculates the minimum time required to break all locks.

        Args:
            strength: A list of integers representing the strength of each lock.
            k: An integer representing the increase in breaking power after breaking each lock.
        Returns:
            An integer representing the minimum total time to break all locks.
        """
        n = len(strength)
        memoStore = {}

        def getMinimum(mask, currentX):
            if mask == (1 << n) - 1:
                return 0

            if mask in memoStore:
                return memoStore[mask]

            minTime = float('inf')

            for i in range(n):
                if not (mask & (1 << i)):
                    timeRequired = (strength[i] + currentX - 1) // currentX
                    remainingTime = getMinimum(mask | (1 << i), currentX + k)
                    totalPathTime = timeRequired + remainingTime

                    if totalPathTime < minTime:
                        minTime = totalPathTime

            memoStore[mask] = minTime
            return minTime

        return getMinimum(0, 1)