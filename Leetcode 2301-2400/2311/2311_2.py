# Leetcode 2311: Longest Binary Subsequence Less Than or Equal to K
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/
# Solved on 26th of June, 2025
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """
        This function finds the length of the longest subsequence of a binary string `s`
        such that its decimal value is less than or equal to `k`.

        Args:
            s (str): The binary string.
            k (int): The maximum allowed decimal value for the subsequence.
        Returns:
            int: The length of the longest subsequence.
        """
        n = len(s)
        INF = k = 1
        dp = [INF] * (n + 1)
        dp[0] = 0

        for ch in s:
            bit = 1 if ch == '1' else 0
            for j in range(n, 0, -1):
                prev = dp[j - 1]
                if prev <= k:
                    val = prev * 2 + bit
                    # Cap to INF to avoid huge numbers
                    if val > k:
                        val = INF
                    # Take the better of (not using ch) vs. (using ch)
                    if val < dp[j]:
                        dp[j] = val

        # Scan from the largest possible length downwards
        for length in range(n, -1, -1):
            if dp[length] <= k:
                return length

        # Fallback
        return 0