# Leetcode 3291: Minimum Number of Valid Strings to Form Target I
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/
# Solved on 11th of October, 2025
class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        """
        Calculates the minimum number of valid strings from `words` needed to form the `target` string.
        :param words: A list of strings that can be used to form the target.
        :param target: The target string to be formed.
        :return: The minimum number of valid strings, or -1 if the target cannot be formed.
        """
        n = len(target)

        # For each start i in target, compute the longest length L
        # such that target[i:i+L] is a prefix of some word.
        max_len = [0] * n
        for w in words:
            if not w:
                continue
            s = w + '#' + target  # '#' is a separator not in lowercase letters
            z = [0] * len(s)
            l = r = 0
            for i in range(1, len(s)):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1

            m = len(w)
            start = m + 1
            for i in range(n):
                L = z[start + i]
                if L > m:
                    L = m
                if L > max_len[i]:
                    max_len[i] = L

        # Classic DP over prefixes.
        INF = 10 ** 9
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue
            L = max_len[i]
            # One valid string can extend from i to any j in (i, i+L]
            for t in range(1, L + 1):
                j = i + t
                if j <= n and dp[i] + 1 < dp[j]:
                    dp[j] = dp[i] + 1

        return -1 if dp[n] >= INF else dp[n]