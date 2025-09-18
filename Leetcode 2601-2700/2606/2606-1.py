# Leetcode 2606: Find the Substring With Maximum Cost
# https://leetcode.com/problems/find-the-substring-with-maximum-cost/
# Solved on 18th of September, 2025
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        """
        Calculates the maximum cost of a substring in 's' based on given character costs.
        Args:
            s (str): The input string.
            chars (str): A string of characters whose costs are explicitly defined.
            vals (list[int]): A list of integer costs corresponding to characters in 'chars'.
        Returns:
            int: The maximum cost of any substring in 's'.
        """
        charValues = {chr(ord('a') + i): i + 1 for i in range(26)}

        for i in range(len(chars)):
            charValues[chars[i]] = vals[i]

        maxSoFar = 0
        currentMax = 0

        for char in s:
            cost = charValues[char]
            currentMax += cost

            if currentMax > maxSoFar:
                maxSoFar = currentMax

            if currentMax < 0:
                currentMax = 0

        return maxSoFar