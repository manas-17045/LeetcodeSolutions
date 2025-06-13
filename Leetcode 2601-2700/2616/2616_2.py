# Leetcode 2616: Minimize the Maximum Difference of Pairs
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
# Solved on 13th of June, 2025

class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        # If we need zero pairs, the max difference is 0 by definition.
        """
        Minimizes the maximum difference among p pairs of numbers from the input array.

        Args:
            nums: A list of integers.
            p: The number of pairs to form.

        Returns:
            The minimum possible value for the maximum difference among the p pairs.
            Returns 0 if p is 0.
        """

        if p == 0:
            return 0

        # Sort the array in ascending order.
        nums.sort()

        # Helper function
        def can_pair(max_diff: int) -> bool:
            count = 0
            i = 1
            n = len(nums)
            # Greedily scan adjacent elements
            while i < n and count < p:
                if nums[i] - nums[i - 1] <= max_diff:
                    count += 1
                    i += 2  # Skip both used elements
                else:
                    i += 1
            return count >= p

        # Binary search for the minimum max difference
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if can_pair(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo