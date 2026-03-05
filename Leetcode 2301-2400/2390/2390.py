# Leetcode 2390: Removing Stars From a String
# https://leetcode.com/problems/removing-stars-from-a-string/
# Solved on 5th of March, 2026
class Solution:
    def removeStars(self, s: str) -> str:
        """
        Removes stars from a string by deleting the star and the closest non-star character to its left.

        :param s: The input string containing lowercase English letters and stars '*'.
        :return: The string after all stars have been removed.
        """
        resultStack = []

        for currentChar in s:
            if currentChar == '*':
                resultStack.pop()
            else:
                resultStack.append(currentChar)

        return "".join(resultStack)