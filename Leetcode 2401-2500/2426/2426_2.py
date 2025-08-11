# Leetcode 2426: Number of Pairs Satisfying Inequality
# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/
# Solved on 12th of August, 2025
import bisect


class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:
        """
        Counts the number of pairs (i, j) such that i < j and nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff.

        Args:
            nums1 (list[int]): The first list of integers.
            nums2 (list[int]): The second list of integers.
            diff (int): The maximum allowed difference.

        Returns:
            int: The number of valid pairs (i, j).
        """
        # Compute a[k] = nums1[k] - num2[k]
        n = len(nums1)
        a = [nums1[i] - nums2[i] for i in range(n)]

        # Coordinate compression on values a[i]
        vals = sorted(set(a))

        # Fenwick / BIT for counts
        m = len(vals)
        bit = [0] * (m + 1)

        def bit_add(idx: int, val: int = 1) -> None:
            while idx <= m:
                bit[idx] += val
                idx += idx & -idx

        def bit_sum(idx: int) -> int:
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & -idx
            return res

        ans = 0
        # Iterate j from 0...(n - 1), for each j count i < j with a[i] <= a[j] + diff
        for j in range(n):
            threshold = a[j] + diff
            # Find rightmost index in vals where value <= threshold
            pos = bisect.bisect_right(vals, threshold)
            if pos > 0:
                ans += bit_sum(pos)
            # Now, add current a[j] to BIT for future indices
            idx = bisect.bisect_left(vals, a[j]) + 1
            bit_add(idx, 1)

        return ans