# Leetcode 3228: Maximum Number of Operations to Move Ones to the End
# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/
# Solved on 13th of November, 2025
class Solution:
    def maxOperations(self, s: str) -> int:
        """
        Calculates the maximum number of operations to move all ones to the end of the binary string.

        Args:
            s (str): The input binary string.
        Returns:
            int: The maximum number of operations.
        """
        totalOperations = 0
        totalOnes = 0
        hasEncounteredZeroBlock = True

        for char in s:
            if char == '1':
                totalOnes += 1
                hasEncounteredZeroBlock = False
            else:
                if not hasEncounteredZeroBlock:
                    totalOperations += totalOnes
                    hasEncounteredZeroBlock = True

        return totalOperations