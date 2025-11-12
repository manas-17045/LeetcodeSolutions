# Leetcode 1806: Minimum Number of Operations to Reinitialize a Permutation
# https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/
# Solved on 12th of November, 2025
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        """
        Calculates the minimum number of operations to reinitialize a permutation.

        Args:
            n (int): The length of the permutation.
        Returns:
            int: The minimum number of operations.
        """
        if n == 2:
            return 1

        count = 0
        currentIndex = 1
        nHalf = n // 2

        while True:
            if currentIndex < nHalf:
                currentIndex = 2 * currentIndex
            else:
                currentIndex = 2 * currentIndex - n + 1

            count += 1
            if currentIndex == 1:
                break

        return count