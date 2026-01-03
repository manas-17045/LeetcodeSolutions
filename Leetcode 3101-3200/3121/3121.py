# Leetcode 3121: Count the Number of Special Characters II
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/
# Solved on 3rd of January, 2026
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        Counts the number of special characters in a given word.
        A character is considered special if its lowercase version appears before its uppercase version.

        Args:
            word (str): The input string.
        Returns:
            int: The count of special characters.
        """
        lastLower = [-1] * 26
        firstUpper = [-1] * 26

        for i, char in enumerate(word):
            if 'a' <= char <= 'z':
                lastLower[ord(char) - ord('a')] = i
            else:
                index = ord(char) - ord('A')
                if firstUpper[index] == -1:
                    firstUpper[index] = i

        specialCount = 0
        for i in range(26):
            if lastLower[i] != -1 and firstUpper[i] != -1:
                if lastLower[i] < firstUpper[i]:
                    specialCount += 1

        return specialCount