# Leetcode 1190: Reverse Substrings Between Each Pair of Parentheses
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# Solved on 27th of September, 2026
class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        Reverses substrings within each pair of matching parentheses from the inside out.

        :param s(str): A string containing lowercase English characters and balanced parentheses.
        :return (str): The resulting string after reversing matching bracket contents and removing parentheses.
        """
        stringLength = len(s)
        bracketStack = []
        pairIndices = [0] * stringLength

        for currentIndex, char in enumerate(s):
            if char == "(":
                bracketStack.append(currentIndex)
            elif char == ")":
                openIndex = bracketStack.pop()
                pairIndices[currentIndex] = openIndex
                pairIndices[openIndex] = currentIndex

        resultChars = []
        currentIndex = 0
        directionStep = 1

        while currentIndex < stringLength:
            if s[currentIndex] in "()":
                currentIndex = pairIndices[currentIndex]
                directionStep = -directionStep
            else:
                resultChars.append(s[currentIndex])

            currentIndex += directionStep

        return "".join(resultChars)