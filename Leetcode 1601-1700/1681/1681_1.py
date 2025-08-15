# Leetcode 1681: Minimum Incompatibility
# https://leetcode.com/problems/minimum-incompatibility/
# Solved on 15th of August, 2025
import itertools
from collections import Counter


class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum incompatibility of an array.

        Args:
            nums (list[int]): The input array of integers.
            k (int): The number of groups to divide the array into.
        Returns:
            int: The minimum incompatibility, or -1 if impossible.
        """

        n = len(nums)
        m = n // k
        freq = Counter(nums)

        if any(f > k for f in freq.values()):
            return -1

        valid = []
        for comb in itertools.combinations(range(n), m):
            values = [nums[i] for i in comb]
            if len(set(values)) == m:
                mn = min(values)
                mx = max(values)
                mask = 0
                for i in comb:
                    mask |= (1 << i)
                valid.append((mask, (mx - mn)))

        INF = 10**9
        dp = [INF] * (1 << n)
        dp[0] = 0

        for _ in range(k):
            newDp = [INF] * (1 << n)
            for mask in range(1 << n):
                if dp[mask] == INF:
                    continue
                for S, c in valid:
                    if (mask & S) == 0:
                        new_mask = mask | S
                        newDp[new_mask] = min(newDp[new_mask], dp[mask] + c)

            dp = newDp

        ans = dp[(1 << n) - 1]
        return ans if ans < INF else -1