# Leetcode 1647: Minimum Deletions to Make Character Frequencies Unique
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# Solved on 21st of August, 2025
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Calculates the minimum number of deletions needed to make all character frequencies unique.

        Args:
            s (str): The input string.
        Returns:
            int: The minimum number of deletions.
        """
        freq = Counter(s)

        if not freq:
            return 0

        f = sorted(freq.values(), reverse=True)

        ans = 0
        prev = f[0]

        for i in range(1, len(f)):
            if f[i] < prev:
                prev = f[i]
            else:
                target = prev - 1
                if target > 0:
                    ans += f[i] - target
                    prev = target
                else:
                    ans += f[i]
                    prev = 0

        return ans