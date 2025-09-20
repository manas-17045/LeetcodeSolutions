# Leetcode 1712: Ways to Split Array Into Three Subarrays
# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
# Solved on 19th of September, 2025
import bisect


class Solution:
    def waysToSplit(self, nums: list[int]) -> int:
        """
        Calculates the number of ways to split an array `nums` into three non-empty contiguous subarrays
        (left, mid, right) such that `sum(left) <= sum(mid) <= sum(right)`.

        Args:
            nums: A list of integers representing the array to be split.

        Returns:
            The number of valid ways to split the array, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(nums)
        if n < 3:
            return 0

        prefix = nums[:]
        for i in range(1, n):
            prefix[i] += prefix[i-1]

        total = prefix[-1]
        ans = 0

        # For each possible left and i (0...(n - 3)), find range of j ((i + 1)...(n - 2))
        for i in range(n - 2):
            left_sum = prefix[i]
            lo = i + 1
            hi_exclusive = n - 1

            j_low = bisect.bisect_left(prefix, 2 * left_sum, lo, hi_exclusive)
            upper_val = (total + left_sum) // 2
            j_high = bisect.bisect_right(prefix, upper_val, lo, hi_exclusive) - 1

            if j_low <= j_high:
                ans += (j_high - j_low + 1)

        return ans % MOD