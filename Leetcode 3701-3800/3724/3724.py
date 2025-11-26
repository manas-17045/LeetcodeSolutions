# Leetcode 3724: Minimum Operations to Transform Array
# https://leetcode.com/problems/minimum-operations-to-transform-array/
# Solved on 26th of November, 2025
class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the minimum operations to transform nums1 into nums2.

        Args:
            nums1: The first list of integers.
            nums2: The second list of integers.
        Returns:
            The minimum number of operations required.
        """
        n = len(nums1)
        totalOps = 0
        minExtraOps = float('inf')
        targetLast = nums2[-1]

        for i in range(n):
            currDiff = abs(nums1[i] - nums2[i])
            totalOps += currDiff

            minVal = min(nums1[i], nums2[i])
            maxVal = max(nums1[i], nums2[i])

            dist = 0
            if targetLast < minVal:
                dist = minVal - targetLast
            elif targetLast > maxVal:
                dist = targetLast - maxVal

            if dist < minExtraOps:
                minExtraOps = dist

        return totalOps + minExtraOps + 1