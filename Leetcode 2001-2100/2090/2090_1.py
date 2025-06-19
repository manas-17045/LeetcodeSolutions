# Leetcode 2090: K Radius Subarray Averages
# https://leetcode.com/problems/k-radius-subarray-problems/
# Solved on 19th of June, 2025

class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        """
        Calculates the k-radius subarray averages for a given array.

        For each index i in the input array nums, the k-radius average is the
        average of all elements in the subarray from index i - k to i + k
        (inclusive). If the subarray is out of bounds, the average is -1.

        Args:
            nums: The input list of integers.
            k: The radius of the subarray.
        """
        numElements = len(nums)
        averages = [-1] * numElements

        if k == 0:
            return nums

        windowSize = 2 * k + 1

        if windowSize > numElements:
            return averages

        currentSum = sum(nums[0: windowSize])
        averages[k] = currentSum // windowSize

        for centerIndex in range((k + 1), (numElements - k)):
            elementToRemove = nums[centerIndex - k - 1]
            elementToAdd = nums[centerIndex + k]

            currentSum = currentSum - elementToRemove + elementToAdd
            averages[centerIndex] = currentSum // windowSize

        return averages