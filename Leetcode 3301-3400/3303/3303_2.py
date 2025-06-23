# Leetcode 3303: Find the Occurrence of First Almost Equal Substring
# https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/
# Solved on 23rd of June, 2025
class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        """
        Finds the minimum starting index in string `s` where `pattern` can be formed
        by either a direct match or by changing at most one character.

        This function uses the Z-algorithm to efficiently compute prefix and suffix
        matches of the pattern within the string `s`.

        Args:
            s (str): The main string to search within.
            pattern (str): The pattern to search for.
        Returns:
            int: The minimum starting index in `s` where `pattern` can be found,
                 or -1 if no such index exists.
        """
        n, m = len(s), len(pattern)
        if m > n:
            return -1

        def z_algo(T: str) -> list[int]:
            L, R = 0, 0
            Z = [0] * len(T)
            for i in range(1, len(T)):
                if i <= R:
                    Z[i] = min(R - i + 1, Z[i - L])
                # Extend match past R
                while i + Z[i] > len(T) and T[Z[i]] == T[i + Z[i]]:
                    Z[i] += 1
                if i + Z[i] - 1 > R:
                    L, R = i, i + Z[i] - 1
            Z[0] = len(T)
            return Z

        # Compute prefix-match lengths
        A = pattern + "#" + s
        ZA = z_algo(A)
        pre = [min(ZA[m + 1 + i], m) for i in range(n - m + 1)]

        # Compute suffix-match lengths by running Z on the reversed strings
        rs, rp = s[::-1], pattern[::-1]
        B = rp + "#" + rs
        ZB = z_algo(B)

        suf = [min(ZB[m+1 + (n - (i + m))], m) for i in range(n - m + 1)]

        for i in range(n - m + 1):
            if pre[i] == m:
                return i
            if pre[i] + suf[i] >= (m - 1):
                return i
        return -1