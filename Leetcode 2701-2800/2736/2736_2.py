# Leetcode 2736: Maximum Sum Queries
# https://leetcode.com/problems/maximum-sum-queries/
# Solved on 7th of July, 2025
import bisect


class Solution:
    def maximumSumQueries(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        """
        Given two 0-indexed integer arrays nums1 and nums2 of length n, and two 0-indexed integer arrays queries of length m,
        where queries[i] = [xi, yi].

        For each query, you need to find the maximum sum nums1[j] + nums2[j] among all indices j such that nums1[j] >= xi and nums2[j] >= yi.
        If no such index j exists, the answer for this query is -1.

        Return an array answer of length m where answer[i] is the answer to the ith query.

        The solution uses a combination of sorting, coordinate compression, and a Fenwick tree (BIT).
        1. Points (nums1[i], nums2[i]) are sorted by nums1[i] in descending order.
        2. Queries (x, y) are sorted by x in descending order.
        3. nums2 values are coordinate-compressed to map them to indices for the Fenwick tree.
        4. The Fenwick tree stores the maximum sum (nums1[j] + nums2[j]) for activated points.
        5. Queries are processed: points satisfying nums1[j] >= x are added to the BIT, and then the BIT is queried for nums2[j] >= y.
        """
        n = len(nums1)
        # prepare and sort the points by nums1 descending
        points = [(nums1[i], nums2[i], (nums1[i] + nums2[i])) for i in range(n)]
        points.sort(key=lambda x: -x[0])

        # Sort queries by x desc, remember original index
        qs = []
        for i, (x, y) in enumerate(queries):
            qs.append((x, y, i))
        qs.sort(key=lambda x: -x[0])

        # Coordinate-compress nums2 values
        Ys = sorted(set(nums2))
        m = len(Ys)

        # Fenwick tree (1...m) supporting point-update max, prefix max query
        INF_NEG = -10**18
        bit = [INF_NEG] * (m + 1)
        def bit_update(i: int, val: int):
            while i <= m:
                if val > bit[i]:
                    bit[i] = val
                i += i & -i

        def bit_query(i: int) -> int:
            ans = INF_NEG
            while i > 0:
                if bit[i] > ans:
                    ans = bit[i]
                i -= i & -i
            return ans

        ans = [-1] * len(queries)
        j = 0   # pointer into points

        # Process each query into descending x
        for x, y, qi in qs:
            # Activate all points with nums1 >= x
            while j < n and points[j][0] >= x:
                _, yval, s = points[j]
                # Find its compressed position
                p = bisect.bisect_left(Ys, yval)    # 0-based
                # Reverse index so that Fenwick prefix = original suffix
                rIdx = m - p
                bit_update(rIdx, s)
                j += 1

            # Answer this query by querying max over all nums2 >= y
            p = bisect.bisect_left(Ys, y)
            if p < m:
                rIdx = m - p
                best = bit_query(rIdx)
                if best > INF_NEG:
                    ans[qi] = best

        return ans