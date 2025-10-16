# Leetcode 2598: Smallest Missing Non-negative Integer After Operations
# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/
# Solved on 16th of October, 2025
class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        """
        Finds the smallest non-negative integer that cannot be formed by taking elements from `nums`
        and applying the modulo operation with `value`.

        Args:
            nums (list[int]): A list of integers.
            value (int): The modulo value.
        Returns:
            int: The smallest non-negative integer that cannot be formed.
        """
        # Count frequency of each remainder class
        remainder_count = [0] * value

        for num in nums:
            remainder = num % value
            remainder_count[remainder] += 1

        # Find the smallest non-negative integer we cannot form
        mex = 0
        while True:
            required_remainder = mex % value

            # Check if we have an element with this remainder available
            if remainder_count[required_remainder] > 0:
                remainder_count[required_remainder] -= 1
                mex += 1
            else:
                # Cannot form this integer
                break

        return mex