# Leetcode 3507: Minimum Pair Removal to Sort Array I
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/
# Solved on 22nd of January, 2026
class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of pair removal operations to sort the array.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The number of operations performed to make the array sorted.
        """
        operations = 0
        while True:
            isSorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    isSorted = False
                    break

            if isSorted:
                return operations

            minSum = float('inf')
            mergeIndex = -1

            for i in range(len(nums) - 1):
                currentSum = nums[i] + nums[i + 1]
                if currentSum < minSum:
                    minSum = currentSum
                    mergeIndex = i

            nums[mergeIndex] = minSum
            nums.pop(mergeIndex + 1)
            operations += 1