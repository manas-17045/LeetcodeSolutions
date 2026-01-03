# Leetcode 3196: Maximize Total Cost of Alternating Subarrays
# https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/
# Solved on 3rd of January, 2026
class Solution:
    def maximumTotalCost(self, nums: list[int]) -> int:
        """
        Calculates the maximum total cost of alternating subarrays.

        Args:
            nums: A list of integers representing the input array.

        Returns:
            An integer representing the maximum total cost.
        """
        lastPlus = nums[0]
        lastMinus = -float('inf')

        for i in range(1, len(nums)):
            currentVal = nums[i]
            nextMinus = lastPlus - currentVal
            lastPlus = max(lastPlus, lastMinus) + currentVal
            lastMinus = nextMinus

        return max(lastPlus, lastMinus)