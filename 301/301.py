# Leetcode 301: Remove Invalid Parentheses
# https://leetcode.com/problems/remove-invalid-parentheses/
# Solved on 7th of October, 2026
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        """
        Removes the minimum number of invalid parentheses to make the input string valid.

        :param s: Input string containing parentheses and lowercase letters.
        :return: Unique valid strings formed by removing minimum invalid parentheses.
        """
        leftRem = 0
        rightRem = 0

        for eachChar in s:
            if eachChar == "(":
                leftRem += 1
            elif eachChar == ")":
                if leftRem > 0:
                    leftRem -= 1
                else:
                    rightRem += 1

        resultSet = set()
        currentChars = []

        self.depthFirstSearch(0, leftRem, rightRem, 0, currentChars, s, resultSet)

        return list(resultSet)

    def depthFirstSearch(
        self,
        charIndex: int,
        leftRem: int,
        rightRem: int,
        openBalance: int,
        currentChars: list[str],
        sourceStr: str,
        resultSet: set[str],
    ) -> None:
        if len(sourceStr) - charIndex < leftRem + rightRem:
            return

        if charIndex == len(sourceStr):
            if leftRem == 0 and rightRem == 0 and openBalance == 0:
                resultSet.add("".join(currentChars))
            return

        currentChar = sourceStr[charIndex]

        if currentChar == "(" and leftRem > 0:
            self.depthFirstSearch(
                charIndex + 1,
                leftRem - 1,
                rightRem,
                openBalance,
                currentChars,
                sourceStr,
                resultSet,
            )
        elif currentChar == ")" and rightRem > 0:
            self.depthFirstSearch(
                charIndex + 1,
                leftRem,
                rightRem - 1,
                openBalance,
                currentChars,
                sourceStr,
                resultSet,
            )

        currentChars.append(currentChar)

        if currentChar == "(":
            self.depthFirstSearch(
                charIndex + 1,
                leftRem,
                rightRem,
                openBalance + 1,
                currentChars,
                sourceStr,
                resultSet,
            )
        elif currentChar == ")":
            if openBalance > 0:
                self.depthFirstSearch(
                    charIndex + 1,
                    leftRem,
                    rightRem,
                    openBalance - 1,
                    currentChars,
                    sourceStr,
                    resultSet,
                )
        else:
            self.depthFirstSearch(
                charIndex + 1,
                leftRem,
                rightRem,
                openBalance,
                currentChars,
                sourceStr,
                resultSet,
            )

        currentChars.pop()