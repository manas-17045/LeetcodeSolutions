# Leetcode 2044: Count Number of Maximum Bitwise-OR Subsets
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
# Solved on 22nd of October, 2024
class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        """
        Counts the number of non-empty subsets of nums whose bitwise OR sum equals the maximum possible bitwise OR sum of any subset.

        :param nums: A list of integers.
        :return: The number of subsets with the maximum bitwise OR sum.
        """

        target = 0
        for num in nums:
            target |= num

        dp = {0: 1}

        for num in nums:
            new_dp = dp.copy()
            for curr_or, count in dp.items():
                new_or = curr_or | num
                new_dp[new_or] = new_dp.get(new_or, 0) + count
            dp = new_dp

        return dp.get(target, 0)