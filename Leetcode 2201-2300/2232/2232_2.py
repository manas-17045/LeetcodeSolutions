# Leetcode 2232: Minimize Result by Adding Parentheses to Expression
# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/
# Solved on 30th of July, 2025
class Solution:
    def minimizeResult(self, expression: str) -> str:
        """
        Minimizes the result of an arithmetic expression by strategically placing a single pair of parentheses.

        Args:
            expression (str): A string representing an arithmetic expression of the form "num1+num2".

        Returns:
            str: The expression with parentheses added to achieve the minimum possible result.
        """
        # Find the '+' index
        plus_idx = expression.index('+')
        best = float('inf')
        answer = ""

        # Try every possible '(' position to the left of '+'
        for i in range(0, plus_idx):
            # Try every possible ')' position to the right of '+'
            for j in range(plus_idx + 2, len(expression) + 1):
                # Split into a, b, c, d
                a = expression[:i]
                b = expression[i:plus_idx]
                c = expression[plus_idx + 1:j]
                d = expression[j:]

                # Convert to ints, treating empty a/d as 1
                a_val = int(a) if a else 1
                b_val = int(b)
                c_val = int(c)
                d_val = int(d) if d else 1

                val = a_val * (b_val + c_val) * d_val
                if val < best:
                    best = val
                    # Rebuild the parenthesized string
                    answer = ((a if a else "") + "(" + b + "+" + c + ")" + (d if d else ""))

        return answer