# Leetcode 1529: Minimum Suffix Flips
# https://leetcode.com/problems/minimum-suffix-flips/
# Solved on 14th of November, 2025
class Solution:
    def minFlips(self, target: str) -> int:
        """
        Calculates the minimum number of flips required to transform a string of '0's to the target string.

        Args:
            target (str): The target binary string.
        Returns:
            int: The minimum number of flips.
        """
        numFlips = 0
        currentState = '0'

        for targetChar in target:
            if targetChar != currentState:
                numFlips += 1
                currentState = '1' if currentState == '0' else '0'

        return numFlips