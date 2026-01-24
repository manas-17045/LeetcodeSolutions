# Leetcode 1877: Minimize Maximum Pair Sum in Array
# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
# Solved on 24th of January, 2026
class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        """
        Minimize the maximum pair sum in the array.

        Args:
            nums (list[int]): A list of integers of even length.

        Returns:
            int: The minimized maximum pair sum.
        """
        nums.sort()

        n = len(nums)
        result = 0

        for i in range(n // 2):
            currentSum = nums[i] + nums[n - 1 - i]
            result = max(result, currentSum)

        return result