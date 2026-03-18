# Leetcode 3868: Minimum Cost to Equalize Arrays Using Swaps
# https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/
# Solved on 18th of March, 2026
class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the minimum number of swaps required to make two arrays equal in frequency.

        :param nums1: List of integers representing the first array.
        :param nums2: List of integers representing the second array.
        :return: The minimum number of swaps needed, or -1 if it's impossible.
        """
        frequencyDiff = {}

        for num in nums1:
            frequencyDiff[num] = frequencyDiff.get(num, 0) + 1

        for num in nums2:
            frequencyDiff[num] = frequencyDiff.get(num, 0) - 1

        minSwaps = 0

        for countDiff in frequencyDiff.values():
            if countDiff % 2 != 0:
                return -1

            if countDiff > 0:
                minSwaps += countDiff // 2

        return minSwaps