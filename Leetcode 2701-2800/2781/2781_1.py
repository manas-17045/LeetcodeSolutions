# Leetcode 2781: Length of the Longest Valid Substring
# https://leetcode.com/problems/length-of-the-longest-valid-substring/
# Solved on 19th of July, 2025
class Solution:
    def longestValidSubstring(self, word: str, forbidden: list[str]) -> int:
        """
        Finds the length of the longest valid substring of 'word' that does not contain any forbidden substrings.
        :param word: The input string.
        :param forbidden: A list of forbidden substrings.
        :return: The length of the longest valid substring.
        """
        forbiddenSet = set(forbidden)
        maxLength = 0
        leftBound = 0

        for rightBound in range(len(word)):
            for start in range(rightBound, max(leftBound, (rightBound - 9)) -1, -1):
                if word[start:rightBound+1] in forbiddenSet:
                    leftBound = start + 1
                    break

            # After the check, the substring word[leftBound:rightBound+1] is valid.
            currentLength = rightBound - leftBound + 1
            maxLength = max(maxLength, currentLength)

        return maxLength