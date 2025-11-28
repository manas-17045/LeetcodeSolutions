# Leetcode 1577: Number of Ways Where Square of Number Is Equal to Product of Two Numbers
# https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/
# Solved on 28th of November, 2025
class Solution:
    def numTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the total number of triplets (i, j, k) such that nums1[i]^2 == nums2[j] * nums2[k]
        or nums2[i]^2 == nums1[j] * nums1[k].
        :param nums1: A list of integers.
        :param nums2: A list of integers.
        :return: The total number of such triplets.
        """
        def getTripletCount(targetList, sourceList):
            frequencyMap = {}
            for num in sourceList:
                if num in frequencyMap:
                    frequencyMap[num] += 1
                else:
                    frequencyMap[num] = 1

            count = 0
            for num in targetList:
                targetSquare = num * num
                for key, value in frequencyMap.items():
                    if targetSquare % key == 0:
                        complement = targetSquare // key
                        if complement in frequencyMap:
                            if key == complement:
                                count += value * (value - 1)
                            else:
                                count += value * frequencyMap[complement]
            return count // 2

        return getTripletCount(nums1, nums2) + getTripletCount(nums2, nums1)