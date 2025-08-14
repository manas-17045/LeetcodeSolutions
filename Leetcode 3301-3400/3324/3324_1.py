# Leetcode 3324: Find the Sequence of Strings Appeared on the Screen
# https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/
# Solved on 14th of August, 2025
class Solution:
    def stringSequence(self, target: str) -> list[str]:
        """
        Generates a sequence of strings that simulate typing the target string.

        :param target: The target string to be typed.
        :return: A list of strings representing the sequence of characters appearing on the screen.
        """
        resultSequence = []
        currentCharList = []

        for targetChar in target:
            currentCharList.append('a')
            resultSequence.append("".join(currentCharList))

            while currentCharList[-1] != targetChar:
                newLastCharCode = ord(currentCharList[-1]) + 1
                currentCharList[-1] = chr(newLastCharCode)
                resultSequence.append("".join(currentCharList))

        return resultSequence