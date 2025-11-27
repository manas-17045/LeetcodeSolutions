# Leetcode 2541: Minimum Operations to make Array Equal II
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/
# Solved on 27th of November, 2025
class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        Calculates the minimum number of operations to make nums1 equal to nums2.
        An operation consists of choosing an index i and either adding k to nums1[i]
        or subtracting k from nums1[i].

        :param nums1: The first list of integers.
        :param nums2: The second list of integers.
        :param k: The integer value to add or subtract in each operation.
        :return: The minimum number of operations, or -1 if it's impossible.
        """
        if k == 0:
            return 0 if nums1 == nums2 else -1

        totalDiff = 0
        positiveDiffSum = 0

        for n1, n2 in zip(nums1, nums2):
            diff = n1 - n2

            if diff % k != 0:
                return -1

            totalDiff += diff
            if diff > 0:
                positiveDiffSum += diff

        if totalDiff != 0:
            return -1

        return positiveDiffSum // k