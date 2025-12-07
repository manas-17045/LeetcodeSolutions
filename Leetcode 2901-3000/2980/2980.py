# Leetcode 2980: Check if Bitwise OR Has Trailing Zeros
# https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/
# Solved on 7th of December, 2025
class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        """
        Checks if there exist two distinct numbers in the input list such that their bitwise OR
        has at least one trailing zero.

        :param nums: A list of integers.
        :return: True if such a pair exists, False otherwise.
        """
        evenCount = 0
        for number in nums:
            if number % 2 == 0:
                evenCount += 1
            if evenCount == 2:
                return True

        return False