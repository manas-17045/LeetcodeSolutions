# Leetcode 1889: Minimum Space Wasted From Packaging
# https://leetcode.com/problems/minimum-space-wasted-from-packaging/
# Solved on 26th of July, 2025
import bisect


class Solution:
    def minWastedSpace(self, packages: list[int], boxes: list[list[int]]) -> int:
        """
        Calculates the minimum wasted space when distributing packages into boxes from different suppliers.

        :param packages: A list of integers representing the sizes of the packages.
        :param boxes: A list of lists of integers, where each inner list represents the box sizes offered by a supplier.
        :return: The minimum wasted space modulo 10^9 + 7, or -1 if it's impossible to fit all packages.
        """

        MOD = 10**9 + 7
        # Sort packages and compute prefix sums
        packages.sort()
        n = len(packages)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + packages[i]
        total_sum = prefix[-1]
        res = float('inf')

        # Iterate over each supplier's boxes
        for bxs in boxes:
            bxs.sort()

            # If largest box can't fit the largest package, skip this supplier.
            if bxs[-1] < packages[-1]:
                continue

            wasted = 0
            prev = 0

            # For each box size, fit as many remaining packages as possible
            for b in bxs:
                # Find the rightmost index, where package size <= box size
                idx = bisect.bisect_right(packages, b)

                if idx > prev:
                    # Number of packages in this range is idx - prev.
                    count = idx - prev
                    # Total space used by boxes of this size
                    wasted += count * n - (prefix[idx] - prefix[prev])
                    prev = idx

                # All packages have been assigned
                if prev == n:
                    break

            res = min(res, wasted)

        return -1 if res == float('inf') else res % MOD