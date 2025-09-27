# Leetcode 3557: Find Maximum Number of Non Intersecting Substrings
# https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/
# Solved on 27th of September, 2025
class Solution:
    def maxSubstrings(self, word: str) -> int:
        """
        Finds the maximum number of non-intersecting substrings of length at least 4.

        :param word: The input string.
        :return: The maximum number of non-intersecting substrings.
        """
        firstSeen = {}
        substringCount = 0

        for i, char in enumerate(word):
            if char in firstSeen:
                startIndex = firstSeen[char]
                length = i - startIndex + 1
                if length >= 4:
                    substringCount += 1
                    firstSeen = {}
            else:
                firstSeen[char] = i

        return substringCount