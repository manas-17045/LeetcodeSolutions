# Leetcode 1896: Minimum Cost to Change the Final Value of Expression
# https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/
# Solved on 22nd of November, 2025
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        """
        Calculates the minimum cost to change the final value of a boolean expression.

        Args:
            expression: A string representing a boolean expression.

        Returns:
            The minimum number of operations required to flip the final value of the expression.
        """
        stackVal = []
        stackOp = []

        def process():
            op = stackOp.pop()
            v2, c2 = stackVal.pop()
            v1, c1 = stackVal.pop()

            if op == '&':
                if v1 == 1 and v2 == 1:
                    stackVal.append((1, min(c1, c2)))
                elif v1 == 0 and v2 == 0:
                    stackVal.append((0, 1 + min(c1, c2)))
                else:
                    stackVal.append((0, 1))
            else:
                if v1 == 0 and v2 == 0:
                    stackVal.append((0, min(c1, c2)))
                elif v1 == 1 and v2 == 1:
                    stackVal.append((1, 1 + min(c1, c2)))
                else:
                    stackVal.append((1, 1))

        for char in expression:
            if char == '0':
                stackVal.append((0, 1))
            elif char == '1':
                stackVal.append((1, 1))
            elif char == '(':
                stackOp.append(char)
            elif char == ')':
                while stackOp and stackOp[-1] != '(':
                    process()
                stackOp.pop()
            elif char in '&|':
                while stackOp and stackOp[-1] != '(':
                    process()
                stackOp.append(char)

        while stackOp:
            process()

        return stackVal[0][1]