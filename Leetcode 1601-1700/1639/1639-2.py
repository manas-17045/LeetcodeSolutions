# Leetcode 1639: Number of Ways to Form a Target String Given a Dictionary
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
# Solved on 25th of August, 2025
class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        """
        Calculates the number of ways to form the target string by picking characters from
        the given words, where characters are picked column by column.
        :param words: A list of strings, all of the same length.
        :param target: The target string to form.
        :return: The number of ways to form the target string modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        if not words or not target:
            return 0

        n = len(words)
        L = len(words[0])
        m = len(target)

        # Count occurrences of each letter in each column
        counts = [[0] * 26 for _ in range(L)]
        for w in words:
            for i, ch in enumerate(w):
                counts[i][ord(ch) - 97] += 1

        # dp[i] = number of ways to form first i characters of target
        dp = [0] * (m + 1)
        dp[0] = 1

        # Iterate columns left-to-right, update dp backwards
        for col in range(L):
            # For each position in target, attempt to use this column's letters
            for j in range(m - 1, -1, -1):
                c_count = counts[col][ord(target[j]) - 97]
                if c_count:
                    dp[j + 1] = (dp[j + 1] + dp[j] * c_count) % MOD

        return dp[m]