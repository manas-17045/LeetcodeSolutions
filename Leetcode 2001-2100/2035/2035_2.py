# Leetcode 2035: Partition Array Into Two Arrays to Minimize Sum Difference
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
# Solved on 29th of June, 2025
import bisect


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        """
        Finds the minimum absolute difference between the sums of two subsets of a given array,
        where each subset contains exactly n elements.

        This problem is solved using the meet-in-the-middle technique.
        """
        # Total length is 2n
        length = len(nums)
        n = length // 2
        left, right = nums[:n], nums[n:]
        total = sum(nums)

        left_sums = [[] for _ in range(n + 1)]
        right_sums = [[] for _ in range(n + 1)]

        # Enumerate all subsets of left half
        for mask in range(1 << n):
            k = mask.bit_count()
            s = 0
            # Accumulate sum for this mask
            for i in range(n):
                if (mask >> i) & 1:
                    s += left[i]
            left_sums[k].append(s)

        # Enumerate all subsets of right half
        for mask in range(1 << n):
            k = mask.bit_count()
            s = 0
            for i in range(n):
                if (mask >> i) & 1:
                    s += right[i]
            right_sums[k].append(s)

        # Sort each list in right_sums for binary search
        for k in range(n + 1):
            right_sums[k].sort()

        best = float('inf')
        half = total / 2.0

        # For each way of taking k from left, we must take (n - k) from right
        for k in range(n + 1):
            target_list = right_sums[n - k]
            for s_left in left_sums[k]:
                # We want s_left + s_right as close as possible to total / 2
                need = half - s_left
                j = bisect.bisect_left(target_list, need)
                # Check candidate at j and (j - 1)
                for idx in ((j - 1), j):
                    if 0 <= idx < len(target_list):
                        s_right = target_list[idx]
                        curr = abs(total - 2 *(s_left + s_right))
                        if curr < best:
                            best = curr
                            if best == 0:
                                return 0

        return int(best)