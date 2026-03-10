# Leetcode 3862: Find the Smallest Balanced Index
# https://leetcode.com/problems/find-the-smallest-balanced-index/
# Solved on 10th of March, 2026
class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        """
        Finds the smallest index i such that the sum of elements to the left of i
        is equal to the product of elements to the right of i.

        :param nums: A list of integers.
        :return: The smallest balanced index, or -1 if no such index exists.
        """
        arrayLength = len(nums)
        maxSum = sum(nums)
        rightProduct = [0] * arrayLength
        currentProduct = 1

        for i in range(arrayLength - 1, -1, -1):
            rightProduct[i] = currentProduct
            currentProduct *= nums[i]
            if currentProduct > maxSum:
                currentProduct = maxSum + 1

        leftSum = 0
        for i in range(arrayLength):
            if leftSum == rightProduct[i]:
                return i
            leftSum += nums[i]

        return -1