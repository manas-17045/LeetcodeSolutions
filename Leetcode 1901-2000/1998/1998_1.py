# Leetcode 1998: GCD Sort of an Array
# https://leetcode.com/problems/gcd-sort-of-an-array/
# Solved on 14th of July, 2025
import math


class Solution:
    def gcdSort(self, nums: list[int]) -> bool:
        """
        Checks if the given array `nums` can be sorted using GCD-based swaps.
        :param nums: A list of integers.
        :return: True if the array can be GCD-sorted, False otherwise.
        """
        maxNum = max(nums)
        parent = list(range(maxNum + 1))

        def findSet(i):
            if parent[i] == i:
                return i
            parent[i] = findSet(parent[i])
            return parent[i]

        def uniteSets(i, j):
            rootI = findSet(i)
            rootJ = findSet(j)
            if rootI != rootJ:
                parent[rootJ] = rootI

        smallestPrimeFactor = list(range(maxNum + 1))
        for i in range(2, int(math.isqrt(maxNum)) + 1):
            if smallestPrimeFactor[i] == i:
                for j in range(i * i, (maxNum + 1), i):
                    if smallestPrimeFactor[j] == j:
                        smallestPrimeFactor[j] = i

        for num in nums:
            tempNum = num
            while tempNum > 1:
                primeFactor = smallestPrimeFactor[tempNum]
                uniteSets(num, primeFactor)
                while tempNum % primeFactor == 0:
                    tempNum //= primeFactor

        sortedNums = sorted(nums)
        for i in range(len(nums)):
            if findSet(nums[i]) != findSet(sortedNums[i]):
                return False

        return True