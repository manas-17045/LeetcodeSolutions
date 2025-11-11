# Leetcode 474: Ones and Zeroes
# https://leetcode.com/problems/ones-and-zeroes/
# Solved on 11th of November, 2025
class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        """
        Finds the maximum number of strings that can be formed from the given array of strings,
        given the maximum number of '0's (m) and '1's (n) allowed.

        :param strs: A list of strings consisting of '0's and '1's.
        :param m: The maximum number of '0's allowed.
        :param n: The maximum number of '1's allowed.
        :return: The maximum number of strings that can be formed.
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            numZeros = s.count('0')
            numOnes = s.count('1')

            for zeroBudget in range(m, numZeros - 1, -1):
                for oneBudget in range(n, numOnes - 1, -1):
                    dp[zeroBudget][oneBudget] = max(
                        dp[zeroBudget][oneBudget],
                        1 + dp[zeroBudget - numZeros][oneBudget - numOnes]
                    )

        return dp[m][n]