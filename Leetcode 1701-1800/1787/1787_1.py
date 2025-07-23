# Leetcode 1787: Make the XOR of All Segments Equal to Zero
# https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/
# Solve on 23rd of July, 2025
import collections


class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of changes needed to make the XOR sum of all segments equal to zero.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The segment length.
        Returns:
            int: The minimum number of changes required.
        """
        numCount = len(nums)
        maxXorValue = 1 << 10
        infinity = float('inf')

        dp = [infinity] * maxXorValue
        dp[0] = 0

        for i in range(k):
            group = nums[i:numCount:k]
            freq = collections.Counter(group)
            size = len(group)

            minPrevChanges = min(dp)

            nextDp = [minPrevChanges + size] * maxXorValue

            for val, count in freq.items():
                for xorSum in range(maxXorValue):
                    if dp[xorSum] != infinity:
                        newXorSum = xorSum ^ val
                        cost = dp[xorSum] + (size - count)
                        nextDp[newXorSum] = min(nextDp[newXorSum], cost)

            dp = nextDp

        return int(dp[0])