# Leetcode 3190: Find Minimum Operations to Make All Elements Divisible by Three
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
# Solved on 22nd of November, 2025
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations required to make all elements in the given list divisible by three.
        An operation consists of incrementing or decrementing an element by 1.

        Args:
            nums: A list of integers.
        Returns:
            The minimum number of operations.
        """
        minimumOps = 0

        for num in nums:
            remainder = num % 3
            if remainder != 0:
                minimumOps += 1

        return minimumOps