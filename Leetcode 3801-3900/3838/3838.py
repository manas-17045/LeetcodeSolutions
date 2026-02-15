# Leetcode 3838: Weighted Word Mapping
# https://leetcode.com/problems/weighted-word-mapping/
# Solved on 15th of February, 2026
class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        """
        Maps each word to a character based on the sum of its character weights.

        :param words: A list of strings to be processed.
        :param weights: A list of 26 integers representing weights for 'a' through 'z'.
        :return: A string formed by the mapped characters of each word.
        """
        resultList = []

        for word in words:
            currentWeight = 0
            for char in word:
                weightIndex = ord(char) - 97
                currentWeight += weights[weightIndex]

            remainderValue = currentWeight % 26
            mappedChar = chr(122 - remainderValue)
            resultList.append(mappedChar)

        return "".join(resultList)