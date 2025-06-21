# Leetcode 3085: Minimum Deletions to Make String K-Special
# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/
# Solved on 21st of June, 2025
import collections


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """
        Calculates the minimum number of deletions required to make the word k-beautiful.

        A word is k-beautiful if for any two character frequencies f1 and f2,
        it holds that |f1 - f2| <= k.

        The approach is to iterate through all possible minimum frequencies (m)
        that characters in the final k-beautiful word could have. For each 'm',
        we calculate the maximum number of characters we can keep.

        :param word: The input string.
        :param k: The maximum allowed difference between any two character frequencies.
        :return: The minimum number of deletions.
        """
        n = len(word)
        freq = list(collections.Counter(word).values())
        if not freq:
            return 0

        maxF = max(freq)
        bestKept = 0

        # Try every possible floor m for kept frequencies
        for m in range(maxF + 1):
            cap = m + k
            kept = 0
            for f in freq:
                if f >= m:
                    # Keep between m and (m + k) of this char
                    kept += min(f, cap)
            bestKept = max(bestKept, kept)

        return n - bestKept