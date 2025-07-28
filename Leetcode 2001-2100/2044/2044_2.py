# Leetcode 2044: Count Number of Maximum Bitwise-OR Subsets
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
# Solved on 28th of July, 2025
class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        """
        Counts the number of non-empty subsets of `nums` whose bitwise OR sum equals the maximum possible bitwise OR sum of any subset.

        Args:
            nums: A list of integers.

        Returns:
            The number of subsets whose bitwise OR sum is equal to the maximum possible bitwise OR sum.
        """
        n = len(nums)
        maxOr = 0
        for num in nums:
            maxOr |= num

        count = 0

        def backtrack(index, currentOr):
            nonlocal count
            if index == n:
                if currentOr == maxOr:
                    count += 1
                return

            backtrack(index + 1, currentOr)

            backtrack(index + 1, currentOr | nums[index])

        backtrack(0, 0)
        return count