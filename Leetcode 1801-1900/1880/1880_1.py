# Leetcode 1880: Check if Word Equals Summation of Two Words
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
# Solved on 2nd of August, 2025
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        """
        Checks if the sum of the numerical values of two words equals the numerical value of a target word.

        Args:
            firstWord (str): The first word.
            secondWord (str): The second word.
            targetWord (str): The target word.
        Returns:
            bool: True if the sum of the numerical values of firstWord and secondWord equals targetWord, False otherwise.
        """
        def getIntValue(word):
            numericValueStr = ""
            for char in word:
                numericValueStr += str(ord(char) - ord('a'))
            return int(numericValueStr)
        
        firstNum = getIntValue(firstWord)
        secondNum = getIntValue(secondWord)
        targetNum = getIntValue(targetWord)

        return firstNum + secondNum == targetNum