# Leetcode 903: Valid Permutations for DI Sequence
# https://leetcode.com/problems/valid-permutations-for-di-sequence/
# Solved on 24th of July, 2025
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        """
        Calculates the number of permutations of (0, 1, ..., n) that satisfy the given DI (decreasing/increasing) sequence.
        :param s: A string consisting of 'D' (decreasing) and 'I' (increasing) characters.
        :return: The number of valid permutations modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(s)
        dp = [1] * (n + 1)

        for i in range(1, (n + 1)):
            ndp = [0] * (n + 1)
            if s[i - 1] == 'I':
                total = 0
                for j in range(n - i + 1):
                    total = (total + dp[j]) % MOD
                    ndp[j] = total
            else:
                total = 0
                for j in range(n - i, -1, -1):
                    total = (total + dp[j + 1]) % MOD
                    ndp[j] = total
            dp = ndp

        return dp[0]