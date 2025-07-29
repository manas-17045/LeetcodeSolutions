# Leetcode 1987: Number of Unique Good Subsequences
# https://leetcode.com/problems/number-of-unique-good-subsequences/
# Solved on 29th of July, 2025
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        """
        Calculates the number of unique "good" subsequences of a binary string.
        A subsequence is "good" if it does not contain leading zeros (unless it's "0" itself).

        Args:
            binary (str): The input binary string.
        Returns:
            int: The number of unique good subsequences modulo 10^9 + 7.
        """
        endsWithZero = 0
        endsWithOne = 0
        hasZero = 0
        mod = 10 ** 9 + 7

        for bit in binary:
            if bit == '1':
                endsWithOne = (endsWithZero + endsWithOne + 1) % mod
            else:
                endsWithZero = (endsWithZero + endsWithOne) % mod
                hasZero = 1

        return (endsWithZero + endsWithOne + hasZero) % mod