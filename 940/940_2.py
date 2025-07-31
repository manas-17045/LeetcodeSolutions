# Leetcode 940: Distinct Subsequences II
# https://leetcode.com/problems/distinct-subsequences-ii/
# Solved on 31st of July, 2025
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """
        Calculates the number of distinct non-empty subsequences of a given string `s`.
        :param s: The input string.
        :return: The number of distinct non-empty subsequences modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        # dp[i] = number of distinct subsequences ending with chr(ord('a') + i)
        dp = [0] * 26
        # Total number of dostinct non-empty subsequences so far
        total = 0

        for ch in s:
            idx = ord(ch) - ord('a')
            # All existing subsequences can be extended by ch, plus the subsequence [ch] itself
            new_count = (total + 1) % MOD
            # To avoid duplicates, oonly add the newly created ones
            added = (new_count - dp[idx] + MOD) % MOD
            # Update total and dp[idx]
            total = (total + added) % MOD
            dp[idx] = new_count

        return total