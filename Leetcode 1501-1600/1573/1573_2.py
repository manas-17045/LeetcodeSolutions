# Leetcode 1573: Number of Ways to Split a String
# https://leetcode.com/problems/number-of-ways-to-split-a-string/
# Solved on 23rd of August, 2025
class Solution:
    def numWays(self, s: str) -> int:
        """
        Calculates the number of ways to split a binary string into three non-empty parts
        such that each part has the same number of '1's.

        Args:
            s (str): The input binary string.
        Returns:
            int: The number of ways to split the string, modulo 10^9 + 7.
        """
        n = len(s)

        if n < 3:
            return 0

        MOD = 10 ** 9 + 7
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if s[i] == '1' else 0)
        total = prefix[n]

        if total % 3 != 0:
            return 0

        target = total // 3
        A = []
        B = []

        for k in range(1, n):
            if prefix[k] == target:
                A.append(k)
            if prefix[k] == 2 * target:
                B.append(k)

        if not A or not B:
            return 0

        ans = 0
        j = 0
        m = len(B)
        for a in A:
            while j < m and B[j] <= a:
                j += 1
            ans = (ans + m - j) % MOD

        return ans