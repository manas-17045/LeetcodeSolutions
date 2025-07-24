# Leetcode 1955: Count Number of Special Subsequences
# https://leetcode.com/problems/count-number-of-special-subsequences/
# Solved on 24th of July, 2025
class Solution:
    def countSpecialSubsequences(self, nums: list[int]) -> int:
        """
        Counts the number of special subsequences in the given list of integers.
        A special subsequence is defined as a subsequence that consists of 0s, followed by 1s, followed by 2s.

        Args:
            nums: A list of integers.
        Returns:
            The number of special subsequences modulo 10^9 + 7.
        """
        endingInZero = 0
        endingInOne = 0
        endingInTwo = 0
        modulo = 10**9 + 7

        for num in nums:
            if num == 0:
                endingInZero = (2 * endingInZero + 1) % modulo
            elif num == 1:
                endingInOne = (2 * endingInOne + endingInZero) % modulo
            elif num == 2:
                endingInTwo = (2 * endingInTwo + endingInOne) % modulo

        return endingInTwo