# Leetcode 1889: Minimum Space Wasted From Packaging
# https://leetcode.com/problems/minimum-space-wasted-from-packaging/
# Solved on 26th of July, 2025
import bisect


class Solution:
    def minWastedSpace(self, packages: list[int], boxes: list[list[int]]) -> int:
        """
        Calculates the minimum space wasted to pack items from a single supplier.

        Args:
            packages: A list of integers representing the sizes of the packages.
            boxes: A 2D list where boxes[i] is a list of box sizes offered by supplier i.

        Returns:
            The minimum total wasted space modulo 10^9 + 7, or -1 if impossible.
        """
        numPackages = len(packages)
        mod = 10**9 + 7

        packages.sort()
        packageSum = sum(packages)

        minWaste = float('inf')

        for boxesForSupplier in boxes:
            boxesForSupplier.sort()

            if packages[numPackages - 1] > boxesForSupplier[-1]:
                continue

            currentSupplierSpace = 0
            lastPackageIdx = 0

            for box in boxesForSupplier:
                packageIdx = bisect.bisect_right(packages, box)

                count = packageIdx - lastPackageIdx
                currentSupplierSpace += count * box
                lastPackageIdx = packageIdx

                if lastPackageIdx == numPackages:
                    break

            waste = currentSupplierSpace - packageSum
            minWaste = min(minWaste, waste)

        if minWaste == float('inf'):
            return -1
        else:
            return minWaste % mod