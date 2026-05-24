# Leetcode 1340: Jump Game V
# https://leetcode.com/problems/jump-game-v/
# Solved on 24th of May, 2026
class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        """
        Calculates the maximum number of indices that can be visited starting from any index.

        :param arr: List of integers representing the heights at each index.
        :param d: Maximum jump distance allowed in either direction.
        :return: The maximum number of indices that can be visited.
        """
        arrayLength = len(arr)
        memoArray = [0] * arrayLength

        def calculateJumps(currIndex):
            if memoArray[currIndex] != 0:
                return memoArray[currIndex]

            maxJumpsCount = 1

            for rightIndex in range(currIndex + 1, min(currIndex + d + 1, arrayLength)):
                if arr[rightIndex] >= arr[currIndex]:
                    break
                maxJumpsCount = max(maxJumpsCount, 1 + calculateJumps(rightIndex))

            for leftIndex in range(currIndex - 1, max(currIndex - d - 1, -1), -1):
                if arr[leftIndex] >= arr[currIndex]:
                    break
                maxJumpsCount = max(maxJumpsCount, 1 + calculateJumps(leftIndex))

            memoArray[currIndex] = maxJumpsCount
            return maxJumpsCount

        overallMaxJumps = 0
        for startIndex in range(arrayLength):
            overallMaxJumps = max(overallMaxJumps, calculateJumps(startIndex))

        return overallMaxJumps