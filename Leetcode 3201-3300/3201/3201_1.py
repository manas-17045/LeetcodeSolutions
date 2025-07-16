# Leetcode 3201: Find the Maximum Length of Valid Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/
# Solved on 16th of July, 2025
class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        """
        Finds the maximum length of a valid subsequence.
        A valid subsequence is one where all elements have the same parity, or parities alternate.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The maximum length of a valid subsequence.
        """
        countEven = 0
        countOdd = 0

        altLength = 0
        lastParity = -1

        for num in nums:
            currentParity = num % 2

            if currentParity == 0:
                countEven += 1
            else:
                countOdd += 1

            if currentParity != lastParity:
                altLength += 1
                lastParity = currentParity

        return max(countEven, countOdd, altLength)