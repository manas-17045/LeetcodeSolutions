# Leetcode 3444: Minimum Increments for Target Multiples in an Array
# https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/
# Solved on 5th of October, 2025
import math


class Solution:
    def minimumIncrements(self, nums: list[int], target: list[int]) -> int:
        """
        Calculates the minimum total increments needed to make each number in `nums`
        a multiple of at least one number from every non-empty subset of `target`.
        :param nums: A list of integers.
        :param target: A list of integers representing the target multiples.
        :return: The minimum total increments required.
        """
        m = len(target)
        full = (1 << m) - 1

        # Precompute lcm for every non-empty subset of targets
        lcm_for_mask = [1] * (1 << m)
        for mask in range(1, 1 << m):
            lowBit = mask & -mask
            prev = mask & -mask
            j = (lowBit.bit_length() - 1)
            a = lcm_for_mask[prev]
            b = target[j]
            l = a // math.gcd(a, b) * b
            lcm_for_mask[mask] = l

        INF = 10**30
        dp = [INF] * (1 << m)
        dp[0] = 0

        # For each number in nums, consider making it a multiple of any subset of targets
        for n in nums:
            # Compute cost for this number to become multiple of each subject
            cost = [0] * (1 << m)
            for mask in range(1, 1 << m):
                L = lcm_for_mask[mask]
                # Minimal increments to reach next multiple of L
                cost[mask] = (L - (n % L)) % L

            newDp = dp[:]
            # Try adding this number with any subset to existing masks
            for cur_mask in range(1 << m):
                if dp[cur_mask] == INF:
                    continue
                base = dp[cur_mask]
                # Iterate non-empty subsets and update
                for sub in range(1, 1 << m):
                    nm = cur_mask | sub
                    val = base + cost[sub]
                    if val < newDp[nm]:
                        newDp[nm] = val
            dp = newDp

        return dp[full]