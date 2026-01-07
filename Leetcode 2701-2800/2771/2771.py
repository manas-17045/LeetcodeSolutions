# Leetcode 2771: Longest Non-decreasing Subarray From Two Arrays
# https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/
# Solved on 7th of January, 2026
class Solution:
    def maxNonDcreasingLength(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the length of the longest non-decreasing subarray that can be formed
        by picking elements from either nums1 or nums2 at each index.

        :param nums1: The first list of integers.
        :param nums2: The second list of integers.
        :return: The length of the longest non-decreasing subarray.
        """
        n = len(nums1)
        dp1 = 1
        dp2 = 1
        maxLength = 1

        for i in range(1, n):
            current1 = 1
            current2 = 1

            if nums1[i] >= nums1[i - 1]:
                current1 = max(current1, dp1 + 1)
            if nums1[i] >= nums2[i - 1]:
                current1 = max(current1, dp2 + 1)

            if nums2[i] >= nums1[i - 1]:
                current2 = max(current2, dp1 + 1)
            if nums2[i] >= nums2[i - 1]:
                current2 = max(current2, dp2 + 1)

            dp1 = current1
            dp2 = current2
            maxLength = max(maxLength, dp1, dp2)

        return maxLength