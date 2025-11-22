# Leetcode 2063: Vowels of All Substrings
# https://leetcode.com/problems/vowels-of-all-substrings/
# Solved on 22nd of November, 2025
class Solution:
    def countVowels(self, word: str) -> int:
        """
        Calculates the total number of vowels across all possible substrings of a given word.

        Args:
            word (str): The input string.
        Returns:
            int: The total count of vowels in all substrings.
        """
        totalCount = 0
        wordLength = len(word)
        for index, char in enumerate(word):
            if char in "aeiou":
                totalCount += (index + 1) * (wordLength - index)

        return totalCount