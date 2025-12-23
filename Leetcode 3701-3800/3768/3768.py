# Leetcode 3768: Minimum Inversion Count in Subarrays of Fixed Length
# https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/
# Solved on 22nd of December, 2025
class Solution:
    def minInversionCount(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum inversion count among all subarrays of a fixed length k.

        Args:
            nums: A list of integers.
            k: The fixed length of the subarrays.
        Returns:
            The minimum inversion count found.
        """
        n = len(nums)
        sortedUnique = sorted(set(nums))
        rankMap = {val: i + 1 for i, val in enumerate(sortedUnique)}
        m = len(sortedUnique)
        ranks = [rankMap[x] for x in nums]

        bit = [0] * (m + 1)

        def update(index, delta):
            while index <= m:
                bit[index] += delta
                index += index & (-index)

        def query(index):
            total = 0
            while index > 0:
                total += bit[index]
                index -= index & (-index)
            return total

        currentInversions = 0
        for i in range(k):
            rank = ranks[i]
            currentInversions += (i - query(rank))
            update(rank, 1)

        minInversions = currentInversions

        for i in range(k, n):
            outRank = ranks[i - k]
            inRank = ranks[i]

            currentInversions -= query(outRank - 1)
            update(outRank, -1)

            currentInversions += (k - 1 - query(inRank))
            update(inRank, 1)

            if currentInversions < minInversions:
                minInversions = currentInversions

        return minInversions