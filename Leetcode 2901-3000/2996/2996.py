# Leetcode 2996: Smallest Missing Integer Greater Than Sequential Prefix Sum
# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
# Solved on 11th of August, 2026
class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        """
        Calculates the smallest missing integer greater than the sequential prefix sum of the array.
        
        @param nums: The input array of integers.
        @return: The smallest missing integer greater than the sequential prefix sum.
        """
        prefixSum = nums[0]
        arrayLength = len(nums)

        for index in range(1, arrayLength):
            if nums[index] == nums[index - 1] + 1:
                prefixSum += nums[index]
            else:
                break

        numSet = set(nums)
        targetValue = prefixSum

        while targetValue in numSet:
            targetValue += 1

        return targetValue