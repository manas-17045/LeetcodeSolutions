# Leetcode 3129: Find All Possible Stable Binary Arrays I
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/
# Solved on 3rd of January, 2026
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        """
        Calculates the number of stable binary arrays with a given number of zeros and ones,
        where no more than 'limit' consecutive identical characters are allowed.

        Args:
            zero (int): The total number of zeros in the array.
            one (int): The total number of ones in the array.
            limit (int): The maximum number of consecutive identical characters allowed.

        Returns:
            int: The number of stable binary arrays modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7
        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]

        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1

        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + mod) % mod

                dp[i][j][1] = (dp[i][j - 1][1] + dp[i][j - 1][0]) % mod
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + mod) % mod

        return (dp[zero][one][0] + dp[zero][one][1]) % mod