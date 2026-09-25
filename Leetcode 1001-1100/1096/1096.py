# Leetcode 1096: Brace Expansion II
# https://leetcode.com/problems/brace-expansion-ii/
# Solved on 25th of September, 2026
from ast import TypeVarTuple
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        """
        Expands the given brace expression into a sorted list of unique words.

        Parameters:
            expression (str): The brace expression to evaluate.

        Returns:
            list[str]: The lexicographically sorted list of unique words represented by the expression.
        """
        resultSet, endIndex = self.parseExpression(expression, 0)
        return sorted(resultSet)

    def parseExpression(self, expressionText: str, startIndex: int) -> tuple[set[str], int]:

        expressionSet = set()
        currentIndex = startIndex
        totalLength = len(expressionText)

        while True:
            termSet, currentIndex = self.parseTerm(expressionText, currentIndex)
            expressionSet |= termSet
            if currentIndex < totalLength and expressionText[currentIndex] == ",":
                currentIndex += 1
            else:
                break
        
        return expressionSet, currentIndex

    def parseTerm(self, expressionText: str, startIndex: int) -> tuple[set[str], int]:

        termSet = {""}
        currentIndex = startIndex
        totalLength = len(expressionText)

        while currentIndex < totalLength and expressionText[currentIndex] not in ",}":
            factorSet, currentIndex = self.parseFactor(expressionText, currentIndex)
            termSet = {
                prefixWord + suffixWord
                for prefixWord in termSet
                for suffixWord in factorSet
            }

        return termSet, currentIndex

    def parseFactor(self, expressionText: str, startIndex: int) -> tuple[set[str], int]:

        if expressionText[startIndex] == "{":
            resultSet, nextIndex = self.parseExpression(expressionText, startIndex + 1)
            return resultSet, nextIndex + 1

        wordChars = []
        currentIndex = startIndex
        totalLength = len(expressionText)

        while currentIndex < totalLength and expressionText[currentIndex].isalpha():
            wordChars.append(expressionText[currentIndex])
            currentIndex += 1

        return {"".join(wordChars)}, currentIndex
        