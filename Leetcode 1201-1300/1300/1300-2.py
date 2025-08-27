# Leetcode 1300: Sum of Mutated Array Closest to Target
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
# Solved on 28th of August, 2025
import bisect


class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        """
        Finds the integer value such that if all elements in `arr` greater than this value are replaced by this value,
        the sum of the modified array is as close as possible to `target`. If there are two such values, return the smaller one.

        :param arr: A list of integers.
        :param target: The target sum.
        :return: The integer value that minimizes the absolute difference between the modified array sum and the target.
        """

        arr.sort()
        n = len(arr)
        prefix = [0] * (n + 1)
        for i, v in enumerate(arr):
            prefix[i + 1] = prefix[i] + v

        def mutated_sum(val: int) -> int:
            idx = bisect.bisect_right(arr, val)
            return prefix[idx] + (n - idx) * val

        lo, hi = 0, arr[-1]
        # Find smallest value such that mutated_sum(value) >= target
        while lo < hi:
            mid = (lo + hi) // 2
            if mutated_sum(mid) < target:
                lo = mid + 1
            else:
                hi = mid

        # Check lo and lo - 1 (and lo could be 0)
        best = lo
        best_diff = abs(mutated_sum(best) - target)

        if best > 0:
            s = mutated_sum(best - 1)
            d = abs(s - target)
            if d < best_diff or (d == best_diff and (best - 1) < best):
                best, best_diff = best - 1, d

        return best