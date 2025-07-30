# Leetcode 2232: Minimize Result by Adding Parentheses to Expression
# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/
# Solved on 30th of July, 2025
class Solution:
    def minimizeResult(self, expression: str) -> str:
        """
        Minimizes the result of an arithmetic expression by adding one pair of parentheses.

        Args:
            expression (str): The input string representing an arithmetic expression of the form "num1+num2".

        Returns:
            str: The expression with parentheses added to achieve the minimum possible result.
        """
        plusIndex = expression.find('+')
        minResult = float('inf')
        resultExpression = ""

        for i in range(plusIndex):
            for j in range(plusIndex + 1, len(expression)):
                leftPart = expression[:i]
                middleLeft = expression[i:plusIndex]
                middleRight = expression[plusIndex + 1:j + 1]
                rightPart = expression[j + 1:]

                valA = 1
                if leftPart:
                    valA = int(leftPart)

                valB = int(middleLeft)
                valC = int(middleRight)

                valD = 1
                if rightPart:
                    valD = int(rightPart)

                currentResult = valA * (valB + valC) * valD

                if currentResult < minResult:
                    minResult = currentResult
                    resultExpression = f"{leftPart}({middleLeft}+{middleRight}){rightPart}"

        return resultExpression