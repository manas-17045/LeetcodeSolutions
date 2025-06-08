# Leetcode 3410: Maximize Subarray Sum After Removing All Occurrences of One Element
# https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/
# Solved on 8th of June, 2025
from collections import defaultdict


class Solution:
    def maxSubarraySum(self, nums: list[int]) -> int:
        """
        Given an integer array nums, you are allowed to remove at most one element.
        Find the maximum sum of a subarray of the remaining elements.

        The sum of an empty subarray is 0.

        This solution uses a segment tree to efficiently query subarray sums and
        related information (prefix sum, suffix sum, best subarray sum) in O(log n) time.
        It first calculates the maximum subarray sum without any removals.
        Then, it iterates through each unique negative number `x` in the array.
        For each `x`, it considers removing all occurrences of `x`. This splits the
        array into segments. The maximum subarray sum after removing `x` is the maximum
        of the best subarray sums within each segment, or the maximum sum formed by
        concatenating a suffix of one segment with a prefix of the next.
        """
        n = len(nums)
        if n == 0:
            return 0

        # Build size = next power of two >= n
        size = 1
        while size < n:
            size <<= 1

        # <<< pad with (0, -inf, -inf, -inf) so empty slots never give sum >= 0
        negInf = float('-inf')
        seg: list[tuple[int, int, int, int]] = [
            (0, negInf, negInf, negInf)
            for _ in range(2 * size)
        ]

        # leaves for real entries
        for i, v in enumerate(nums):
            seg[size + 1] = (v, v, v, v)

        # Build internal nodes
        def merge(A, B):
            total = A[0] + B[0]
            pref = max(A[1], A[0] + B[1])
            suf = max(B[2], A[2] + B[0])
            best = max(A[3], B[3], A[2] + B[1])
            return (total, pref, suf, best)

        for p in range(size - 1, 0, -1):
            seg[p] = merge(seg[2 * p], seg[2 * (p + 1)])

        # Range query [l...r] inclusive
        def query(l: int, r: int) -> tuple[int, int, int, int]:
            l += size; r += size
            left_res = None
            right_res = None
            while l <= r:
                if (l & 1):
                    left_res = seg[l] if left_res is None else merge(left_res, seg[l])
                    l += 1
                if not (r & 1):
                    right_res = seg[r] if right_res is None else merge(seg[r], right_res)
                    r -= 1
                l //= 2; r //= 2
            if left_res is None:
                return right_res
            if right_res is None:
                return left_res
            return merge(left_res, right_res)

        # (1) Base answer: no removal
        ans = seg[1][3]

        # Gather positions
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        # (2) Try removing each negative x (positives won't help)
        for x, plist in pos.items():
            if x >= 0 or len(plist) == n:
                continue
            bounds = [-1] + plist + [n]
            currSuf = negInf
            bestX = negInf

            for i in range(len(bounds) - 1):
                l = bounds[i] + 1
                r = bounds[i + 1] - 1
                if l > r:
                    continue
                tsum, tp, ts, tb = query(l, r)
                if currSuf == negInf:
                    # First Segment
                    currSuf = ts
                    bestX = tb
                else:
                    # Concat
                    bestX = max(bestX, tb, currSuf + tp)
                    currSuf = max(ts, tsum + currSuf)
            ans = max(ans, bestX)

        return ans