# Leetcode 3250: Find the Count of Monotonic Pairs I
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/
# Solved on 11th of September, 2025
class Solution:
    def countOfPairs(self, nums: list[int]) -> int:
        """
        Calculates the number of pairs (a, b) such that 0 <= a_i <= nums[i] for all i,
        and |a_i - a_{i-1}| <= nums[i] - nums[i-1] for all i > 0.

        Args:
            nums: A list of integers representing the upper bounds for each a_i.
        Returns:
            The total number of valid sequences 'a' modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        if n == 0:
            return 0

        maxv = max(nums)
        # prev[val] = number of ways for previous index with a_prev = val
        prev = [0] * (maxv + 1)
        # base: for i = 0, any a0 in [0, nums[0]] is valid
        for v in range(nums[0] + 1):
            prev[v] = 1

        for i in range(1, n):
            cur = [0] * (maxv + 1)
            delta = max(0, nums[i] - nums[i - 1])

            # Build prefix sums of prev for fast range sums
            prefix = [0] * (maxv + 1)
            running = 0
            for k in range(maxv + 1):
                running = (running + prev[k]) % MOD
                prefix[k] = running

            # for each possible a[i] (val), sum all prev[a_prev] where
            # a_prev <= val - delta and a_prev <= nums[i-1]
            for val in range(nums[i] + 1):
                upper = val - delta
                if upper < 0:
                    continue
                # prev values only exist up to nums[i-1]
                upper = min(upper, nums[i - 1])
                cur[val] = prefix[upper]

            prev = cur

        # Total ways are sum of dp at last index for a_last in [0, nums[-1]]
        return sum(prev[: nums[-1] + 1]) % MOD