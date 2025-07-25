# Leetcode 3487: Maximum Unique Subarray Sum After Deletion
# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/
# Solved on 25th of July, 2025
class Solution:
    def maxSum(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of a non-empty subarray, with a specific optimization:
        if there are any positive numbers, the optimal sum is the sum of all unique positive numbers.
        Otherwise, it's the largest single number in the array.

        Args:
            nums: A list of integers.
        Returns:
            The maximum sum of a non-empty subarray based on the described logic.
        """
        seen = set()
        pos_sum = 0

        # Sum each unique positive exactly once
        for x in nums:
            if x > 0 and x not in seen:
                seen.add(x)
                pos_sum += x

        # If we get any positive sum, that's optimal.
        if pos_sum > 0:
            return pos_sum

        # Otherwise, we must pick a non-empty subarray; pick the largest element.
        return max(nums)