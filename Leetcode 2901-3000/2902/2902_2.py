# Leetcode 2902: Count of Sub-Multisets With Bounded Sum
# https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/
# Solved on 8th of August, 2025
from collections import Counter


class Solution:
    def countSubMultisets(self, nums: list[int], l: int, r: int) -> int:
        """
        Counts the number of multisets whose sum is within the range [l, r].

        Args:
            nums (list[int]): A list of integers representing the available numbers.
            l (int): The lower bound of the sum range.
            r (int): The upper bound of the sum range.
        Returns:
            int: The number of multisets whose sum is within [l, r], modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        freq = Counter(nums)
        # Handle zeros separately
        zero_count = freq.pop(0, 0)

        dp = [0] * (r + 1)
        dp[0] = 1

        # Process each positive value with its bounded count
        for val, cnt in freq.items():
            if val <= 0:
                # Should not happen since zeros removed, but be safe
                continue
            if val > r:
                continue

            dp_prev = dp[:]
            for rem in range(val):
                max_t = (r - rem) // val
                if max_t < 0:
                    continue
                window = 0
                # Iterate t from 0...max_t where s = rem + t * val
                for t in range(max_t + 1):
                    s = rem + t * val
                    # Include dp_prev[s] into window
                    window = (window + dp_prev[s]) % MOD
                    # If window includes more than (cnt+1) terms, remove the oldest (t - (cnt+1))
                    if t - cnt - 1 >= 0:
                        old_idx = rem + (t - cnt - 1) * val
                        window = (window - dp_prev[old_idx]) % MOD
                    # Now window == sum_{j=0..min(t,cnt)} dp_prev[s - j*val]
                    dp[s] = window

        # Account for zeros: each computed multiset can be combined with 0..zero_count zeros
        if zero_count:
            mult = (zero_count + 1) % MOD
            for i in range(r + 1):
                dp[i] = (dp[i] * mult) % MOD

        # Sum answers in [l, r]
        ans = sum(dp[l:r + 1]) % MOD
        return ans