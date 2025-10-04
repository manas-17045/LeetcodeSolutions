# Leetcode 3584: Maximum Product of First and Last Elements of a Subsequence
# https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/
# Solved on 4th of October, 2025
class Solution:
    def maximumProduct(self, nums: list[int], m: int) -> int:
        """
        Calculates the maximum product of two numbers in a list `nums` such that their indices
        are at least `m` apart.

        Args:
            nums (list[int]): The input list of integers.
            m (int): The minimum distance required between the indices of the two chosen numbers.

        Returns:
            int: The maximum product found.
        """
        n = len(nums)
        max_product = float('-inf')

        # Initialize with the first element
        max_first = nums[0]
        min_first = nums[0]

        # For each possible last element position (must be at least m-1 from start)
        for i in range(m - 1, n):
            # Current element is the last element
            last = nums[i]

            # Calculate products with both max and min
            product1 = max_first * last
            product2 = min_first * last

            max_product = max(max_product, product1, product2)

            # Update max_first and min_first by including the new valid first element
            # The next valid first element position is i - m + 2
            if i - m + 2 < n:
                new_first = nums[i - m + 2]
                max_first = max(max_first, new_first)
                min_first = min(min_first, new_first)

        return max_product