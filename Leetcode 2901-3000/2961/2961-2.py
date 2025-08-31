# Leetcode 2961: Double Modular Exponentiation
# https://leetcode.com/problems/double-modular-exponentiation/
# Solved on 31st of August, 2025
class Solution:
    def getGoodIndices(self, variables: list[list[int]], target: int) -> list[int]:
        """
        Calculates good indices based on specific modular exponentiation conditions.

        Args:
            variables (list[list[int]]): A list of lists, where each inner list contains [a, b, c, m] values.
            target (int): The target value to match.
        Returns:
            list[int]: A list of indices where the calculated value equals the target.
        """
        res: list[int] = []
        for i, (a, b, c, m) in enumerate(variables):
            base = pow(a, b, 10)
            val = pow(base, c, m)
            if val == target:
                res.append(i)
        return res