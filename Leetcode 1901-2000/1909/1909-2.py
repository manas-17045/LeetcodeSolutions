# Leetcode 1909: Remove One Element to Make the Array Strictly Increasing
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
# Solved on 5th of September, 2025
class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        """
        Determines if an array can be made strictly increasing by removing at most one element.
        :param nums: A list of integers.
        :return: True if the array can be made strictly increasing, False otherwise.
        """
        removed = False

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                # Already removed one element before
                if removed:
                    return False
                removed = True

                # Decide whether to remove nums[i - 1] or nums[i]
                if i > 1 and nums[i] <= nums[i - 2]:
                    # Virtually remove nums[i]
                    nums[i] = nums[i - 1]

        return True