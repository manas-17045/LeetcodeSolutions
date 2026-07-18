# Leetcode 3974: Maximum Total Sum of K Selected Elements
# https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/
# Solved on 18th of July, 2026
class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        """
        Finds the maximum total sum of k selected elements from the array.

        Args:
            nums: The input array of integers.
            k: The number of elements to select.
            mul: The multiplier.

        Returns:
            The maximum total sum of k selected elements.
        """
        nums.sort(reverse=True)
        totalSum = 0

        for i in range(k):
            currentMul = max(1, mul - i)
            totalSum += nums[i] * currentMul
        
        return totalSum