# Leetcode 1537: Get the Maximum Score
# https://leetcode.com/problems/get-the-maximum-score/
# Solved on 27th of July, 2025
class Solution:
    def maxSum(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the maximum score you can get by traversing two sorted arrays.
        You can switch between arrays at common elements.

        Args:
            nums1 (list[int]): The first sorted array of distinct integers.
            nums2 (list[int]): The second sorted array of distinct integers.
        Returns:
            int: The maximum score modulo 10^9 + 7.
        """

        lenOne = len(nums1)
        lenTwo = len(nums2)
        i = 0
        j = 0
        sumOne = 0
        sumTwo = 0
        modVal = 10 ** 9 + 7

        while i < lenOne and j < lenTwo:
            if nums1[i] < nums2[j]:
                sumOne += nums1[i]
                i += 1
            elif nums2[j] < nums1[i]:
                sumTwo += nums2[j]
                j += 1
            else:
                pathValue = max(sumOne, sumTwo) + nums1[i]
                sumOne = pathValue
                sumTwo = pathValue
                i += 1
                j += 1

        while i < lenOne:
            sumOne += nums1[i]
            i += 1

        while j < lenTwo:
            sumTwo += nums2[j]
            j += 1

        return max(sumOne, sumTwo) % modVal