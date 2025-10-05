# Leetcode 3686: Number of Stable Subsequences
# https://leetcode.com/problems/number-of-stable-subsequences/
# Solved on 5th of October, 2025
class Solution:
    def countStableSubsequences(self, nums: list[int]) -> int:
        """
        Counts the number of stable subsequences in the given list of integers.
        A subsequence is stable if the parity of adjacent elements alternates.

        Args:
            nums: A list of integers.
        Returns:
            The total number of stable subsequences modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7

        endsOneOdd = 0
        endsTwoOdd = 0
        endsOneEven = 0
        endsTwoEven = 0

        for num in nums:
            if num % 2 != 0:
                newlyCreatedOneOdd = (1 + endsOneEven + endsTwoEven) % mod
                newlyCreatedTwoOdd = endsOneOdd

                endsOneOdd = (endsOneOdd + newlyCreatedOneOdd) % mod
                endsTwoOdd = (endsTwoOdd + newlyCreatedTwoOdd) % mod
            else:
                newlyCreatedOneEven = (1 + endsOneOdd + endsTwoOdd) % mod
                newlyCreatedTwoEven = endsOneEven

                endsOneEven = (endsOneEven + newlyCreatedOneEven) % mod
                endsTwoEven = (endsTwoEven + newlyCreatedTwoEven) % mod

        totalStableSubsequences = (endsOneOdd + endsTwoOdd + endsOneEven + endsTwoEven) % mod

        return totalStableSubsequences