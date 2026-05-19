# Leetcode 2540: Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/
# Solved on 19th of May, 2026
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Finds the minimum common integer between two sorted arrays.

        :param nums1: A sorted list of integers.
        :param nums2: A sorted list of integers.
        :return: The smallest common integer, or -1 if no common integer exists.
        """
        indexOne = 0
        indexTwo = 0
        lenOne = len(nums1)
        lenTwo = len(nums2)

        while indexOne < lenOne and indexTwo < lenTwo:
            if nums1[indexOne] == nums2[indexTwo]:
                return nums1[indexOne]
            elif nums1[indexOne] < nums2[indexTwo]:
                indexOne += 1
            else:
                indexTwo += 1

        return -1