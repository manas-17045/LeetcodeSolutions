# Leetcode 2317: Maximum XOR After Operations
# https://leetcode.com/problems/maximum-xor-after-operations/
# Solved on 28th of August, 2025
class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        """
        Calculates the maximum possible XOR sum of a subsequence of `nums`.

        Args:
            nums: A list of integers.
        Returns:
            The maximum possible XOR sum.
        """
        res = 0
        for v in nums:
            res |= v

        return res