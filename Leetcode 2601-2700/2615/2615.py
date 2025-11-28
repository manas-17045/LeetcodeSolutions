# Leetcode 2615: Sum of Distances
# https://leetcode.com/problems/sum-of-distances/
# Solved on 28th of November, 2025
class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        """
        Calculates the sum of distances for each element in the input array.

        Args:
            nums: A list of integers.
        Returns:
            A list of integers, where each element result[i] is the sum of |i - j| for all j such that nums[i] == nums[j].
        """
        indexMap = {}
        for i, val in enumerate(nums):
            if val not in indexMap:
                indexMap[val] = []
            indexMap[val].append(i)

        result = [0] * len(nums)
        for indices in indexMap.values():
            totalSum = sum(indices)
            prefixSum = 0
            size = len(indices)

            for i, index in enumerate(indices):
                leftSum = index * i - prefixSum
                rightSum = (totalSum - prefixSum - index) - index * (size - 1 - i)
                result[index] = leftSum + rightSum
                prefixSum += index

        return result