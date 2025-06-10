# Leetcode 2449: Minimum Number of Operations to make Arrays Similar
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/
# Solved on 10th of June, 2025

class Solution:
    def makeSimilar(self, nums: list[int], target: list[int]) -> int:
        """
        Calculates the minimum number of operations to make the array nums similar to the array target.
        An operation consists of adding or subtracting 2 from an element in nums.
        Two arrays are similar if they have the same frequency of each number.

        Args:
            nums: The input list of integers.
            target: The target list of integers.

        Returns:
            The minimum number of operations required.
        """
        # Split nums and target into odd and even lists
        odd_nums, even_nums = [], []
        odd_t, even_t = [], []

        for a, b in zip(nums, target):
            if a & 1:
                odd_nums.append(a)
            else:
                even_nums.append(a)
            if b & 1:
                odd_t.append(b)
            else:
                even_t.append(b)

        # They must have the same counts per parity by problem guarantee
        odd_nums.sort()
        odd_t.sort()
        even_nums.sort()
        even_t.sort()

        # Count how +2's we need
        ops = 0

        # For each parity group, pair up sorted elements
        for x, y in zip(even_nums, even_t):
            if x < y:
                ops += (y - x) // 2
        for x, y in zip(odd_nums, odd_t):
            if x < y:
                ops += (y - x) // 2

        # ops is exactly the minimum number of operations
        return ops