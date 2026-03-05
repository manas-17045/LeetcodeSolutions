# Leetcode 1775: Equal Sum Arrays With Minimum Number of Operations
# https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/
# Solved on 5th of March, 2026
class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the minimum number of operations to make the sum of two arrays equal.
        Each operation involves changing any value in either array to any value between 1 and 6.

        :param nums1: List of integers representing the first array.
        :param nums2: List of integers representing the second array.
        :return: Minimum operations required, or -1 if it is impossible.
        """
        lenOne = len(nums1)
        lenTwo = len(nums2)

        if lenOne > lenTwo * 6 or lenTwo > lenOne * 6:
            return -1

        sumOne = sum(nums1)
        sumTwo = sum(nums2)

        if sumOne == sumTwo:
            return 0

        if sumOne > sumTwo:
            larger = nums1
            smaller = nums2
            diff = sumOne - sumTwo
        else:
            larger = nums2
            smaller = nums1
            diff = sumTwo - sumOne

        gainCounts = [0] * 6

        for num in smaller:
            gainCounts[6 - num] += 1

        for num in larger:
            gainCounts[num - 1] += 1

        operations = 0

        for gain in range(5, 0,-1):
            if diff <= 0:
                break

            if gainCounts[gain] > 0:
                opsNeeded = min(gainCounts[gain], (diff + gain - 1) // gain)
                operations += opsNeeded
                diff -= opsNeeded * gain

        return operations