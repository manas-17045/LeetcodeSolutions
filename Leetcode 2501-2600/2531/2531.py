# Leetcode 2531: Make Number of Distinct Characters Equal
# https://leetcode.com/problems/make-number-of-distinct-characters-equal/
# Solved on 2nd of December, 2025
from collections import Counter


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        """
        Given two 0-indexed strings word1 and word2, swap one character from word1 with one character from word2.
        Return true if it is possible to make the number of distinct characters in word1 and word2 equal, and false otherwise.

        :param word1: The first string.
        :param word2: The second string.
        :return: True if it is possible to make the number of distinct characters in word1 and word2 equal, False otherwise.
        """
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        distinct1 = len(freq1)
        distinct2 = len(freq2)

        for c1 in freq1:
            for c2 in freq2:
                if c1 == c2:
                    if distinct1 == distinct2:
                        return True
                    continue

                newDistinct1 = distinct1
                if freq1[c1] == 1:
                    newDistinct1 -= 1
                if freq1[c2] == 0:
                    newDistinct1 += 1

                newDistinct2 = distinct2
                if freq2[c2] == 1:
                    newDistinct2 -= 1
                if freq2[c1] == 0:
                    newDistinct2 += 1

                if newDistinct1 == newDistinct2:
                    return True

        return False