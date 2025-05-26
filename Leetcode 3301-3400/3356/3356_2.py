# Leetcode 3356: Zero Array Transformation II
# https://leetcode.com/problems/zero-array-transformation-ii/
# Solved on 25th of May, 2025

class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Finds the minimum number of initial queries required to make all elements in `nums` non-negative.

        Args:
            nums: A list of integers representing the initial array.
            queries: A list of queries, where each query is [l, r, v] representing
                     adding v to nums[l] through nums[r].

        Returns:
            The minimum number of queries needed, or -1 if it's impossible to make all elements non-negative.
        """
        n, m = len(nums), len(queries)

        # check if first k queries suffice to cover each nums[i]
        def ok(k: int) -> bool:
            # build diff array for [0..n)
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < n:
                    diff[r + 1] -= v
            cur = 0
            # accumulate and verify
            for i in range(n):
                cur += diff[i]
                if cur < nums[i]:
                    return False
            return True

        # binary search on k in [0..m]
        lo, hi = 0, m
        ans = m + 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans if ans <= m else -1