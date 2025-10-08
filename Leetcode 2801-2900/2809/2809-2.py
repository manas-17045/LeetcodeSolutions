# Leetcode 2809: Minimum Time to Make Array Sum At Most x
# https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/
# Solved on 8th of October, 2025
class Solution:
    def minimumTime(self, nums1: list[int], nums2: list[int], x: int) -> int:
        """
        Calculates the minimum time required to reduce the total sum of elements in nums1
        to be less than or equal to x.

        Args:
            nums1: A list of integers representing initial values.
            nums2: A list of integers representing the increment rate for each element in nums1.
            x: An integer representing the target maximum sum.
        Returns:
            The minimum time (number of operations) required, or -1 if it's not possible.
        """
        n = len(nums1)

        # Initial sum
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        # If already satisfied
        if sum1 <= x:
            return 0

        # Sort by nums2 values (we want to zero larger nums2[i] at later times)
        pairs = sorted(zip(nums2, nums1))

        # dp[t] = maximum reduction we can achieve using exactly t operations
        # at time t (where we do one operation per second)
        dp = [0] * (n + 1)

        # For each element (in sorted order by nums2)
        for a, b in pairs:
            # Process in reverse to avoid using same element twice
            new_dp = dp[:]
            for t in range(1, n + 1):
                # If we zero this element at time t, we save: b + a * t
                # (initial value + all increments up to time t)
                new_dp[t] = max(new_dp[t], dp[t - 1] + b + a * t)
            dp = new_dp

        # Check each possible time from 0 to n
        for t in range(n + 1):
            # Sum at time t = sum1 + sum2 * t - dp[t]
            if sum1 + sum2 * t - dp[t] <= x:
                return t

        return -1