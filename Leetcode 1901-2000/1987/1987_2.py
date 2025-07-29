# Leetcode 1987: Number of Unique Good Subsequences
# https://leetcode.com/problems/number-of-unique-good-subsequences/
# Solved on 29th of July, 2025
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        """
        Calculates the number of unique "good" subsequences of a binary string.
        A subsequence is "good" if it does not contain leading zeros (unless it's "0" itself).

        Args:
            binary (str): The input binary string consisting of '0's and '1's.
        Returns:
            int: The number of unique good subsequences, modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7

        dp0 = 0
        dp1 = 0

        # track whether we've seen at least one '0' (so the single "0" subsequence counts)
        seen_zero = False

        for ch in binary:
            if ch == '1':
                # Any existing subseq ending in 0 or 1 can append '1',
                # plus the new subseq consisting of just "1".
                dp1 = (dp0 + dp1 + 1) % MOD
            else:  # ch == '0'
                # Any existing subseq ending in 0 or 1 can append '0'
                dp0 = (dp0 + dp1) % MOD
                seen_zero = True

        # Sum subseqs ending in '0' and ending in '1', and
        # add 1 if we ever saw a '0' (for the lone "0" subsequence).
        return (dp0 + dp1 + (1 if seen_zero else 0)) % MOD