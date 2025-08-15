# Leetcode 1681: Minimum Incompatibility
# https://leetcode.com/problems/minimum-incompatibility/
# Solved on 15th of August, 2025
import math


class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum total incompatibility of distributing numbers into k subsets.

        Args:
            nums: A list of integers.
            k: The number of subsets to distribute the numbers into.
        Returns:
            The minimum total incompatibility, or -1 if it's impossible to distribute.
        """
        n = len(nums)
        m = n // k
        # Quick impossibility check: a value cannot appear more than k times
        from collections import Counter
        cnt = Counter(nums)
        if any(v > k for v in cnt.values()):
            return -1

        full = (1 << n) - 1

        # Precompute all valid subsets of size m with no duplicate values,
        # and their incompatibility (max - min).
        valid_subsets = []  # list of (mask, incompatibility)
        for mask in range(1 << n):
            if mask.bit_count() != m:
                continue
            seen = set()
            mn = math.inf
            mx = -math.inf
            ok = True
            bit = mask
            idx = 0
            # Iterate through bits
            while bit:
                # Isolate lowest set bit
                lowBit = bit & -bit
                j = (lowBit.bit_length() - 1)  # index of that bit
                val = nums[j]
                if val in seen:
                    ok = False
                    break
                seen.add(val)
                if val < mn:
                    mn = val
                if val > mx:
                    mx = val
                bit ^= lowBit
            if ok:
                valid_subsets.append((mask, mx - mn))

        # If no valid subset exists but k>0 -> impossible
        if not valid_subsets and n != 0:
            return -1

        INF = 10 ** 18
        dp = [INF] * (1 << n)
        dp[0] = 0

        # DP over masks: add one valid subset at a time
        for mask in range(1 << n):
            if dp[mask] == INF:
                continue
            # Try to place any valid subset disjoint with current mask
            for s_mask, cost in valid_subsets:
                if mask & s_mask:
                    continue
                new_mask = mask | s_mask
                if dp[new_mask] > dp[mask] + cost:
                    dp[new_mask] = dp[mask] + cost

        return dp[full] if dp[full] < INF else -1