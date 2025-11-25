# Leetcode 1855: Maximum Distance Between a Pair of Values
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
# Solved on 25th of November, 2025
class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Given two non-increasingly sorted integer arrays nums1 and nums2, return the maximum distance.
        An index pair (i, j) is a valid pair if both i <= j and nums1[i] <= nums2[j].
        The distance of an index pair (i, j) is j - i.

        :param nums1: A list of integers sorted in non-increasing order.
        :param nums2: A list of integers sorted in non-increasing order.
        :return: The maximum distance between a valid pair (i, j).
        """
        idx1 = 0
        idx2 = 0
        maxSeparation = 0
        len1 = len(nums1)
        len2 = len(nums2)

        while idx1 < len1 and idx2 < len2:
            if nums1[idx1] > nums2[idx2]:
                idx1 += 1
            else:
                currentSeparation = idx2 - idx1
                if currentSeparation > maxSeparation:
                    maxSeparation = currentSeparation
                idx2 += 1

        return maxSeparation