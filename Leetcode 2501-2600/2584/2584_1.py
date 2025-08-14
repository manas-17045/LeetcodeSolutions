# Leetcode 2584: Split the Array to Make Coprime Products
# https://leetcode.com/problems/split-the-array-to-make-coprime-products/
# Solved on 14th of August, 2025
class Solution:
    def findValidSplit(self, nums: list[int]) -> int:
        """
        Finds the smallest index `i` such that the product of elements in `nums[0...i]`
        and the product of elements in `nums[i+1...n-1]` are coprime.
        :param nums: A list of integers.
        :return: The smallest valid split index `i`, or -1 if no such split exists.
        """
        limit = 1000001
        spf = list(range(limit))
        i = 2
        while i * i < limit:
            if spf[i] == i:
                for j in range(i * i, limit, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1

        lastOccurrence = {}
        for i, num in enumerate(nums):
            val = num
            while val > 1:
                primeFactor = spf[val]
                lastOccurrence[primeFactor] = i
                while val % primeFactor == 0:
                    val //= primeFactor

        n = len(nums)
        maxReach = 0
        for i in range(n - 1):
            val = nums[i]
            while val > 1:
                primeFactor = spf[val]
                maxReach = max(maxReach, lastOccurrence[primeFactor])
                while val % primeFactor == 0:
                    val //= primeFactor

            if maxReach == i:
                return i

        return -1