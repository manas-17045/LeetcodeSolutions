# Leetcode 3504: Longest Palindrome After Substring Concatenation II
# https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/
# Solved on 9th of December, 2025
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        """
        Finds the length of the longest palindrome that can be formed by concatenating a prefix of s and a suffix of t.

        Args:
            s: The first string.
            t: The second string.
        Returns:
            The length of the longest palindrome.
        """
        n = len(s)
        m = len(t)

        maxPalPrefixS = [0] * (n + 1)
        for i in range(2 * n - 1):
            l, r = i // 2, i // 2 + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxPalPrefixS[l]:
                    maxPalPrefixS[l] = r - l + 1
                l -= 1
                r += 1

        maxPalSuffixT = [0] * (m + 1)
        for i in range(2 * m - 1):
            l, r = i // 2, i // 2 + i % 2
            while l >= 0 and r < m and t[l] == t[r]:
                if r - l + 1 > maxPalSuffixT[r + 1]:
                    maxPalSuffixT[r + 1] = r - l + 1
                l -= 1
                r += 1

        ans = 0
        if maxPalPrefixS:
            ans = max(ans, max(maxPalPrefixS))
        if maxPalSuffixT:
            ans = max(ans, max(maxPalSuffixT))

        tRev = t[::-1]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == tRev[j - 1]:
                    matchLen = dp[i - 1][j - 1] + 1
                    dp[i][j] = matchLen

                    if i < n + 1:
                        cand1 = maxPalPrefixS[i] + 2 * matchLen
                        if cand1 > ans:
                            ans = cand1

                    tSplitIdx = m - j
                    if tSplitIdx >= 0:
                        cand2 = maxPalSuffixT[tSplitIdx] + 2 * matchLen
                        if cand2 > ans:
                            ans = cand2

        return ans