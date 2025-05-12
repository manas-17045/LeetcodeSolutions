# Leetcode 3151: Special Array I
# https://leetcode.com/problems/special-array-i/

class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        """
        Given a 0-indexed integer array nums, an array is considered special if for every index i except the last one, nums[i] and nums[i + 1] have different parities.

        Return true if nums is a special array, otherwise, return false.

        Example 1:
        Input: nums = [2,1,4]
        Output: true
        """
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True