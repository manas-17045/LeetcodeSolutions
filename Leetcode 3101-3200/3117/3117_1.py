# Leetcode 3117: Minimum Sum of Values by Dividing Array
# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/
# Solved on 31st of May, 2025
import math


class SegmentTree:
    def __init__(self, n_orig: int, arr: list[float] | None = None):
        self.n_orig = n_orig
        self.tree_size = 2 * n_orig
        self.tree = [math.inf] * self.tree_size

        if arr:
            for i in range(n_orig):
                self.tree[self.n_orig + i] = arr[i]
            for i in range(self.n_orig - 1, 0, -1):
                self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, l_orig: int, r_orig: int) -> float:
        if l_orig > r_orig or l_orig < 0 or r_orig >= self.n_orig:
            return math.inf

        l = l_orig + self.n_orig
        r = r_orig + self.n_orig + 1

        res = math.inf
        while l < r:
            if l % 2 == 1:
                res = min(res, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = min(res, self.tree[r])

            l //= 2
            r //= 2

        return res

class Solution:
    def minimumValueSelf(self, nums: list[int], andValues: list[int]) -> int:
        """
        Calculates the minimum sum of values by dividing the array `nums` into `m` segments
        such that the bitwise AND of each segment equals the corresponding value in `andValues`.

        Args:
            nums: The input array of integers.
            andValues: The array of target bitwise AND values for each segment.

        Returns:
            The minimum possible sum of the last elements of each segment, or -1 if no such division exists.
        """
        n = len(nums)
        m = len(andValues)

        # dp[k_idx][j]: min sum for andValues[0...k_idx] where these k_idx + 1 segments partition nums[0...j]
        # The (k_idx)-th segment (0-indexed) ends at nums[j].
        dp = [[math.inf] * n for _ in range(m)]

        # Base case: k_idx = 0 (for andValues[0])
        # The first segment must be nums[0...j] and its AND must be andValues[0].
        # current_prefix_and stores nums[0] & nums[1] & ... & nums[j]
        # Represents all bits set (identity for bitwise AND with positive numbers)
        current_prefix_and = -1
        for j in range(n):
            if current_prefix_and == -1:
                current_prefix_and = nums[j]
            else:
                current_prefix_and &= nums[j]

            if current_prefix_and == andValues[0]:
                dp[0][j] = nums[j]

        # Fill DP table for i_idx from 1 to (m - 1) (for andValues[k_idx])
        for k_idx in range(1, m):
            # Segment Tree on dp values for the previous set of segments (ending at andValues[k_idx - 1])
            st = SegmentTree(n, dp[k_idx - 1])

            active_ands: list[tuple[int, int]] = []

            for j in range(k_idx, n):
                newActiveAnds = [(nums[j], j)]
                for prevVal, prevStartIdx in active_ands:
                    currentAnd = prevVal & nums[j]
                    if newActiveAnds[-1][0] == currentAnd:
                        newActiveAnds[-1] = (currentAnd, prevStartIdx)
                    else:
                        newActiveAnds.append((currentAnd, prevStartIdx))
                active_ands = newActiveAnds

                sPrevBoundary = j + 1
                for valTupleVal, valTupleSK in active_ands:
                    if valTupleVal == andValues[k_idx]:
                        minXForCurrentSegment = max(valTupleSK, k_idx)
                        maxXForCurrentSegment = sPrevBoundary - 1

                        if minXForCurrentSegment <= maxXForCurrentSegment:
                            minPrevSum = st.query(minXForCurrentSegment - 1, maxXForCurrentSegment - 1)

                            if minPrevSum != math.inf:
                                dp[k_idx][j] = min(dp[k_idx][j], minPrevSum + nums[j])

                    sPrevBoundary = valTupleSK

        # The result is dp[m - 1][n - 1] as all m segments must partition the entire nums array (nums[0...n-1]).
        minTotalSum = dp[m - 1][n - 1]

        return minTotalSum if minTotalSum != math.inf else -1