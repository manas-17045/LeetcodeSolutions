# Leetcode 3192: Minimum Operations to Make Binary Array Elements Equal to One II
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/
# Solved on 19th of June, 2025

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        """
        Calculates the minimum number of operations to make all elements in the array equal to 1.

        An operation consists of flipping a 0 to a 1 and a 1 to a 0 for the current element
        and all subsequent elements in the array.

        Args:
            nums: A list of integers (0s and 1s).

        Returns:
            The minimum number of operations required.
        """
        flip = 0
        # Flip tracks the parity of flips app,lied so far to the suffix.
        for x in nums:
            # Current value after all previous flips
            if x ^ flip == 0:
                # Perform a flip at this index
                ans += 1
                # Toggle the flip parity for future elements
                flip ^= 1

        return ans