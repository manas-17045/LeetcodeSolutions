# Leetcode 2607: Make K-Subarray Sums Equal
# https://leetcode.com/problems/make-k-subarray-sums-equal/
# Solved on 30th of September, 2025
import math


class Solution:
    def makeSubKSumEqual(self, arr: list[int], k: int) -> int:
        """
        Calculates the minimum number of operations to make all k-sum subarrays equal.

        Args:
            arr: A list of integers representing the array.
            k: An integer representing the subarray length.

        Returns:
            The minimum number of operations required.
        """
        n = len(arr)
        g = math.gcd(n, k)
        ops = 0

        # There are g independent cycles (indices connected by +k mod n).
        cycle_len = n // g
        for start in range(g):
            vals = []
            j = start
            for _ in range(cycle_len):
                vals.append(arr[j])
                j = (j + k) % n

            vals.sort()
            median = vals[cycle_len // 2]

            # Cost to make all values in this cycle equal to median
            ops += sum(abs(v - median) for v in vals)

        return ops