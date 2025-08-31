# Leetcode 2770: Maximum Number of Jumps to Reach the Last Index
# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/
# Solved on 31st of August, 2025
class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        """
        Calculates the maximum number of jumps to reach the last index.

        Args:
            nums (list[int]): A list of integers representing the jump points.
            target (int): The maximum allowed absolute difference between two jump points.
        Returns:
            int: The maximum number of jumps to reach the last index, or -1 if it's not possible.
        """
        numCount = len(nums)
        dp = [-1] * numCount
        dp[0] = 0

        for i in range(1, numCount):
            for j in range(i):
                if dp[j] != -1:
                    difference = nums[i] - nums[j]
                    if -target <= difference <= target:
                        dp[i] = max(dp[i], dp[j] + 1)

        return dp[numCount - 1]