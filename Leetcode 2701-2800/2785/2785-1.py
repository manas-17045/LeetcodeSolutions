# Leetcode 2785: Sort Vowels in a String
# https://leetcode.com/problems/sort-vowels-in-a-string/
# Solved on 11th of September, 2025
class Solution:
    def sortVowels(self, s: str) -> str:
        """
        Sorts the vowels within a given string while maintaining the positions of consonants.

        :param s: The input string.
        :return: The string with vowels sorted in ascending order.
        """

        vowelSet = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        extractedVowels = []
        for char in s:
            if char in vowelSet:
                extractedVowels.append(char)

        extractedVowels.sort()

        resultChars = list(s)
        vowelIndex = 0

        for i in range(len(resultChars)):
            if resultChars[i] in vowelSet:
                resultChars[i] = extractedVowels[vowelIndex]
                vowelIndex += 1

        return "".join(resultChars)