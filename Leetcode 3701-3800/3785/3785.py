# Leetcode 3785: Minimum Swaps to Avoid Forbidden Values
# https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/
# Solved on 24th of December, 2025
from collections import Counter


class Solution:
    def minSwaps(self, nums: list[int], forbidden: list[int]) -> int:
        """
        Calculates the minimum number of swaps required to avoid forbidden values at specific indices.

        Args:
            nums: A list of integers representing the initial array.
            forbidden: A list of integers representing the forbidden values at corresponding indices.

        Returns:
            The minimum number of swaps needed. Returns -1 if it's impossible to avoid all forbidden values.
        """
        n = len(nums)
        numsCount = Counter(nums)
        forbiddenCount = Counter(forbidden)

        for val, count in numsCount.items():
            if count > n - forbiddenCount[val]:
                return -1

        conflictCounts = Counter()
        totalConflicts = 0

        for i in range(n):
            if nums[i] == forbidden[i]:
                conflictCounts[nums[i]] += 1
                totalConflicts += 1

        if totalConflicts == 0:
            return 0

        maxConflictFreq = max(conflictCounts.values())

        return max((totalConflicts + 1) // 2, maxConflictFreq)