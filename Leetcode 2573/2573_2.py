# Leetcode 2573: Find the String with LCP
# https://leetcode.com/problems/find-the-string-with-lcp/
# Solved on 18th of May, 2025

class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        """
        Finds the lexicographically smallest string that matches the given LCP matrix.

        Args:
            lcp: A list of lists representing the Longest Common Prefix (LCP) matrix.
                 lcp[i][j] is the length of the longest common prefix of the substrings
                 starting at indices i and j.

        Returns:
            The lexicographically smallest string that matches the given LCP matrix,
            or an empty string if no such string exists.

        Raises:
            None.
        """
        n = len(lcp)
        # Quick check: diagonal must be n - i
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        word = [''] * n
        next_char = ord('a')

        # Greedily assign characters
        for i in range(n):
            if not word[i]:
                if next_char > ord('z'):
                    return ""   # Ran out of letters
                word[i] = chr(next_char)
                next_char += 1

            # Propagate equalities from LCP: j > i with lcp[i][j] > 0 must share word[i]
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    word[j] = word[i]

        # Now validate by recomputing LCP matrix
        # We only need the diagonal and upper triangle to compare
        # Build a DP row for the next row's lcp; reuse a single list to save space
        nxt = [0] * (n + 1) # Sentinel for out-of-bounds
        for i in range(n - 1, -1, -1):
            cur = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    cur[j] = 1 + nxt[j + 1]
                # else remaines 0
                # Early bail if mismatch
                if cur[j] != lcp[i][j]:
                    return ""
            nxt = cur

        return "".join(word)