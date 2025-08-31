# Leetcode 1664: Ways to Make a Fair Array
# https://leetcode.com/problems/ways-to-make-a-fair-array/
# Solved on 31st of August, 2025
class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        """
        Calculates the number of ways to make an array fair by removing one element.
        An array is considered fair if the sum of elements at even indices equals the sum of elements at odd indices.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The number of ways to make the array fair.
        """
        # Sum of values at even and odd indices on the right (initially whole array)
        right_even = sum(nums[i] for i in range(0, len(nums), 2))
        right_odd = sum(nums[i] for i in range(1, len(nums), 2))

        left_even = 0
        left_odd = 0
        ways = 0

        for i, v in enumerate(nums):
            # Remove current value from right side sums
            if i % 2 == 0:
                right_even -= v
            else:
                right_odd -= v

            # After removal, elements to the right flip parity.
            if left_even + right_odd == left_odd + right_even:
                ways += 1

            # Move current value into left sums for next iterations
            if i % 2 == 0:
                left_even += v
            else:
                left_odd += v

        return ways