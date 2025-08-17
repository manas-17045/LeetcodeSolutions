# Leetcode 2484: Count Palindromic Subsequences
# https://leetcode.com/problems/count-palindromic-subsequences/
# Solved on 17th of August, 2025
class Solution:
    def countPalindromes(self, s: str) -> int:
        """
        Counts the number of palindromic subsequences of length 5 in the given string s.

        Args:
            s (str): The input string consisting of digits.
        Returns:
            int: The total count of palindromic subsequences of length 5, modulo 10^9 + 7.
        """
        n = len(s)
        if n < 5:
            return 0

        mod = 10**9 + 7
        sInt = [int(c) for c in s]

        left = [[[0] * 10 for _ in range(10)] for _ in range(n + 1)]
        prefixCounts = [0] * 10
        for i in range(n):
            digit = sInt[i]
            for d1 in range(10):
                for d2 in range(10):
                    left[i + 1][d1][d2] = left[i][d1][d2]

            for d1 in range(10):
                left[i + 1][d1][digit] += prefixCounts[d1]

            prefixCounts[digit] += 1

        right = [[[0] * 10 for _ in range(10)] for _ in range(n + 1)]
        suffixCounts = [0] * 10
        for i in range(n - 1, -1, -1):
            digit = sInt[i]
            for d1 in range(10):
                for d2 in range(10):
                    right[i][d1][d2] = right[i + 1][d1][d2]

            for d2 in range(10):
                right[i][digit][d2] += suffixCounts[d2]

            suffixCounts[digit] += 1

        totalCount = 0
        for k in range(2, n - 2):
            for d1 in range(10):
                for d2 in range(10):
                    countLeft = left[k][d1][d2]
                    countRight = right[k + 2][d2][d1]
                    term = countLeft * countRight
                    totalCount = (totalCount + term) % mod

        return totalCount