# Leetcode 903: Valid Permutations for DI Sequence
# https://leetcode.com/problems/valid-permutations-for-di-sequence/
# Solved on 24th of July, 2025
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        """
        Calculates the number of valid permutations for a given DI sequence.

        Args:
            s (str): The DI sequence string, consisting of 'D' (decreasing) and 'I' (increasing) characters.
        Returns:
            int: The number of valid permutations modulo 10^9 + 7.
        """
        stringLength = len(s)
        mod = 10**9 + 7

        dp = [1]

        for i in range(1, (stringLength + 1)):
            character = s[i - 1]
            nextDp = [0] * (i + 1)

            if character == 'I':
                currentSum = 0
                for j in range(i + 1):
                    nextDp[j] = currentSum
                    if j < i:
                        currentSum = (currentSum + dp[j]) % mod
            else:
                currentSum = 0
                for j in range(i, -1, -1):
                    nextDp[i] = currentSum
                    if j > 0:
                        currentSum = (currentSum + dp[j - 1]) % mod

            dp = nextDp

        return sum(dp) % mod