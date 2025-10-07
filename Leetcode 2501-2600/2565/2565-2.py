# Leetcode 2565: Subsequence With the Minimum Score
# https://leetcode.com/problems/subsequence-with-the-minimum-score/
# Solved on 6th of October, 2025
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        """
        Calculates the minimum score required to make 't' a subsequence of 's'.
        The score is defined as the minimum number of characters to remove from 't'.

        Args:
            s (str): The main string.
            t (str): The target string to be a subsequence.
        Returns:
            int: The minimum number of characters to remove from 't'.
        """
        n, m = len(s), len(t)

        pref = [-1] * m
        i, j = 0, 0
        while i < n and j < m:
            if s[i] == t[j]:
                pref[j] = i
                j += 1
            i += 1

        # If the whole t is already a subsequence -> score 0
        if m == 0 or pref[-1] != -1:
            # If t is empty or fully matched, no removals needed.
            return 0

        suff = [-1] * m
        i, j = n - 1, m - 1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                suff[j] = i
                j -= 1
            i -= 1

        # Two-pointer sweep to find minimal removal span
        ans = m
        j = 0
        # Iterate i over -1...(m - 1) where i is the last kept index on the left
        for i in range(-1, m):
            if i >= 0 and pref[i] == -1:
                break
            left_pos = pref[i] if i >= 0 else -1
            # Move j to the smallest index > i such that suffix starting at j can be matched after left_pos
            while j < m and (j <= i or suff[j] <= left_pos):
                j += 1
            ans = min(ans, j - i - 1)

        return ans