# Leetcode 3978: Maximum Valid Pair Sum
# https://leetcode.com/problems/maximum-valid-pair-sum/
# Solved on 26th of July, 2026
class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum sum of any pair (nums[i], nums[j]) such that the conditions are satisfied.
        @param nums: The array of integers.
        @param k: The constraint for the pair sum.
        @return: The maximum valid pair sum.
        """
        maxLeft = 0
        maxSum = nums[0] + nums[k]

        for index in range(k, len(nums)):
            maxLeft = max(maxLeft, nums[index - k])
            maxSum = max(maxSum, maxLeft + nums[index])

        return maxSum