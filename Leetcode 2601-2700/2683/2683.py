# Leetcode 2683: Neighboring Bitwise XOR
# https://leetcode.com/problems/neighboring-bitwise-xor/
# Solved on 12th of November, 2025
class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        """
        Determines if a valid original array exists such that its neighboring bitwise XOR
        results in the given derived array.

        Args:
            derived: A list of integers representing the derived array.
        Returns:
            True if a valid original array exists, False otherwise.
        """
        xorSum = 0
        for num in derived:
            xorSum ^= num

        return xorSum == 0