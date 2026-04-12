# Leetcode 3891: Minimum Increase to Maximize Special Indices
# https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/
# Solved on 12th of April, 2026
class Solution:
    def minIncrease(self, nums: list[int]) -> int:
        """
        Calculates the minimum total increase required to maximize the number of special indices.

        :param nums: A list of integers representing the input array.
        :return: An integer representing the minimum number of operations needed.
        """
        listLength = len(nums)

        if listLength % 2 != 0:
            totalOperations = 0
            for i in range(1, listLength - 1, 2):
                cost = max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])
                totalOperations += cost
            return totalOperations

        currentOperations = 0
        for i in range(2, listLength - 1, 2):
            cost = max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])
            currentOperations += cost

        minimumOperations = currentOperations

        for i in range(1, listLength - 1, 2):
            oddCost = max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])
            evenIndex = i + 1
            evenCost = max(0, max(nums[evenIndex - 1], nums[evenIndex + 1]) + 1 - nums[evenIndex])

            currentOperations += oddCost - evenCost
            if currentOperations < minimumOperations:
                minimumOperations = currentOperations

        return minimumOperations