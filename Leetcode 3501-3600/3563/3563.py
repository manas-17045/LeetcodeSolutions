# Leetcode 3563: Lexicographically Smallest String After Adjacent Removals
# https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/
# Solved on 17th of December, 2025
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        """
        Finds the lexicographically smallest string after performing adjacent removals.

        Args:
            s (str): The input string.
        Returns:
            str: The lexicographically smallest string.
        """
        n = len(s)
        nums = [ord(c) for c in s]

        removable = [[False] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for k in range(i + 1, j + 1, 2):
                    d = nums[i] - nums[k]
                    if d == 1 or d == -1 or d == 25 or d == -25:

                        if i + 1 > k - 1 or removable[i + 1][k - 1]:

                            if k + 1 > j or removable[k + 1][j]:
                                removable[i][j] = True
                                break

        dp = [""] * (n + 1)

        for i in range(n - 1, -1, -1):
            best_s = s[i] + dp[i + 1]

            for k in range(i + 1, n, 2):
                d = nums[i] - nums[k]
                if d == 1 or d == -1 or d == 25 or d == -25:
                    if i + 1 > k - 1 or removable[i + 1][k - 1]:
                        candidate = dp[k + 1]
                        if candidate < best_s:
                            best_s = candidate

            dp[i] = best_s

        return dp[0]