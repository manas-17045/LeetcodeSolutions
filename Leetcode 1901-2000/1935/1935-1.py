# Leetcode 1935: Maximum Number of Words You Can Type
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/
# Solved on 15th of September, 2025
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Calculates the number of words in a given text that can be typed,
        given a set of broken letters.
        :param text: The input string containing words separated by spaces.
        :param brokenLetters: A string containing all characters that are broken.
        :return: The number of words that can be typed.
        """
        brokenSet = set(brokenLetters)
        wordList = text.split(' ')
        typeableWordCount = len(wordList)

        for word in wordList:
            for char in word:
                if char in brokenSet:
                    typeableWordCount -= 1
                    break

        return typeableWordCount