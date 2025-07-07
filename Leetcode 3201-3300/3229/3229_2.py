# Leetcode 3229: Minimum Operations to Make Array Equal to Target
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/
# Solved on 7th of July, 2025
class Solution:
    def minimumOperations(self, nums: list[int], target: list[int]) -> int:
        """
        Calculates the minimum operations to make the array `nums` equal to `target`.

        This problem can be thought of as a 1D version of the "Painting a Fence" problem
        or "Building a Skyline" problem. We are interested in the net change in operations
        needed as we iterate through the array.

        Args:
            nums: The initial array of integers.
            target: The target array of integers.

        Returns:
            The minimum number of operations required.
        """
        inc_ops = 0

        dec_ops = 0
        prev = 0

        for a, b in zip(nums, target):
            diff = b - a
            if diff > 0:
                # Positive segment
                if prev > 0:
                    # Only pay for any extra rise
                    inc_ops += max(diff - prev, 0)
                else:
                    # We're coming from <= 0, pay for the full climb.
                    inc_ops += diff
            elif diff < 0:
                # Negative segment
                if prev < 0:
                    # Only pay for any extra drop
                    dec_ops += max(diff - prev, 0)
                else:
                    # Coming from >= 0, pay for full drop
                    dec_ops += -diff

            prev = diff

        return inc_ops + dec_ops