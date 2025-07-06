# Leetcode 2945: Find Maximum Non-decreasing Array Length
# https://leetcode.com/problems/find-maximum-non-decreasing-array-length/
# Solved on 6th of July, 2025
import bisect


class Solution:
    def findMaximumLength(self, nums: list[int]) -> int:
        """
        Finds the maximum number of non-empty subarrays such that the sum of elements
        in each subarray is greater than or equal to the sum of elements in the previous subarray.

        Args:
            nums: A list of integers.
        Returns:
            The maximum possible length `k`.
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dp = [0] * (n + 1)
        lastVal = [0] * (n + 1)

        monoQueue = [(0, (0, 0))]

        for i in range(1, (n + 1)):
            idx = bisect.bisect_right(monoQueue, (prefix[i], (float('inf'), float('inf')))) - 1

            bestDpVal, bestPrefixVal = monoQueue[idx][1]

            dp[i] = bestDpVal + 1
            lastVal[i] = prefix[i] - bestPrefixVal

            currentCost = prefix[i] + lastVal[i]
            newEntry = (currentCost, (dp[i], prefix[i]))

            while monoQueue and ((monoQueue[-1][0] >= newEntry[0]) or (monoQueue[-1][1] >= newEntry[1])):
                monoQueue.pop()

            monoQueue.append(newEntry)

        return dp[n]