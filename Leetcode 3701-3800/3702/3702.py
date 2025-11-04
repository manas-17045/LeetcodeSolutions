# Leetcode 3702: Longest Subsequence With Non-Zero Bitwise XOR
# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/
# Solved on 4th of November, 2025
class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        """
        Calculates the length of the longest subsequence with a non-zero bitwise XOR sum.

        Args:
            nums: A list of integers.
        Returns:
            The length of the longest subsequence with a non-zero bitwise XOR sum.
        """
        totalXor = 0
        hasNonZero = False

        for num in nums:
            totalXor ^= num
            if num != 0:
                hasNonZero = True

        if totalXor != 0:
            return len(nums)

        if hasNonZero:
            return len(nums) - 1

        return 0