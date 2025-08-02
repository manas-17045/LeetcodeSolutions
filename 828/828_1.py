# Leetcode 828: Count Unique Characters of All Substrings of a Given String
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
# Solved on 2nd of August, 2025
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        Calculates the total number of unique characters across all substrings of a given string.

        For each character, it determines how many substrings it contributes to as a unique character.
        This is done by considering its previous and next occurrences.

        Args:
            s (str): The input string.
        Returns:
            int: The total sum of unique characters across all substrings.
        """
        indexMap = {}
        totalSum = 0
        n = len(s)

        for i in range(n):
            char = s[i]
            if char not in indexMap:
                indexMap[char] = []
            indexMap[char].append(i)

        for char in indexMap:
            indices = indexMap[char]
            paddedIndices = [-1] + indices + [n]
            for i in range(1, len(paddedIndices) - 1):
                previndex = paddedIndices[i - 1]
                currentIndex = paddedIndices[i]
                nextIndex = paddedIndices[i + 1]
                leftContribution = currentIndex - previndex - 1
                rightContribution = nextIndex - currentIndex - 1
                totalSum += leftContribution * rightContribution

        return totalSum