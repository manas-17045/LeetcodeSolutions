# Leetcode 3598: Longest Common Prefix Between Adjacent Strings After Removals
# https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/
# Solved on 13th of September, 2025
class Solution:
    def longestCommonPrefix(self, words: list[str]) -> list[int]:
        """
        Calculates the longest common prefix (LCP) for each word in a list of words,
        considering the scenario where that word is removed.

        Args:
            words: A list of strings.
        Returns:
            A list of integers, where each element at index `i` represents the maximum LCP
            possible among the remaining words if `words[i]` were removed.
        """
        n = len(words)
        if n <= 2:
            return [0] * n

        # Helper function to get LCP length of two strings
        def lcpLength(a: str, b: str) -> int:
            m = min(len(a), len(b))
            i = 0
            # Iterate until mismatch
            while i < m and a[i] == b[i]:
                i += 1
            return i

        # Precompute LCP for each pair i between words[i] and words[i + 1]
        m = n - 1
        lcp = [0] * m
        for i in range(m):
            lcp[i] = lcpLength(words[i], words[i + 1])

        # Prefix max and suffix max on LCP array
        prefix_max = [0] * m
        sMax = 0
        for i in range(m):
            if lcp[i] > sMax:
                sMax = lcp[i]
            prefix_max[i] = sMax

        suffix_max = [0] * m
        sMax = 0
        for i in range(m - 1, -1, -1):
            if lcp[i] > sMax:
                sMax = lcp[i]
            suffix_max[i] = sMax

        ans = [0] * n
        for i in range(n):
            # Left region: lcp indices (0...(i - 2))
            left_max = prefix_max[i - 2] if (i - 2) >= 0 else 0
            # Right region: lcp indices ((i + 1)...(m - 1))
            right_max = suffix_max[i + 1] if (i + 1) <= (m - 1) else 0

            # New pair formed by words[i - 1] and words[i = 1] after removing words[i]
            mid = 0
            if 0 < i < (n - 1):
                mid = lcpLength(words[i - 1], words[i + 1])

            ans[i] = max(left_max, right_max, mid)

        return ans