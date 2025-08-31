# Leetcode 2961: Double Modular Exponentiation
# https://leetcode.com/problems/double-modular-exponentiation/
# Solved on 31st of August, 2025
class Solution:
    def getGoodIndices(self, variables: list[list[int]], target: int) -> list[int]:
        """
        Finds indices of variables that satisfy a double modular exponentiation condition.

        Args:
            variables: A list of lists, where each inner list `[a, b, c, m]` represents the parameters for the calculation.
            target: The target value that the final modular exponentiation result should match.
        Returns:
            A list of integers representing the indices of the 'good' variables.
        """
        goodIndices = []
        for i, var in enumerate(variables):
            a = var[0]
            b = var[1]
            c = var[2]
            m = var[3]

            termOne = pow(a, b, 10)
            termTwo = pow(termOne, c, m)

            if termTwo == target:
                goodIndices.append(i)

        return goodIndices