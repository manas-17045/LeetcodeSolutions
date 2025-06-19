# Leetcode 2779: Maximum Beauty of an Array After Applying Operation
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/
# Solved on 19th of June, 2025

class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        """
        Given a 0-indexed integer array nums and a non-negative integer k.

        You can apply the following operation on the array any number of times:

        Choose any index i and replace nums[i] with any integer in the range [nums[i] - k, nums[i] + k].
        Return the maximum possible length of a subarray of nums that is beautiful.

        A subarray is beautiful if all of its elements are equal.
        """
        nums.sort()

        leftIndex = 0
        maxLength = 0
        listLength = len(nums)

        for rightIndex in range(listLength):
            while nums[rightIndex] - nums[leftIndex] > 2 * k:
                leftIndex += 1

            currentLength = rightIndex - leftIndex + 1
            if currentLength > maxLength:
                maxLength = currentLength

        return maxLength