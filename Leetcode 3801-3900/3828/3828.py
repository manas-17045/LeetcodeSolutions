# Leetcode 3828: Final Element After Subarray Deletions
# https://leetcode.com/problems/final-element-after-subarray-deletions/
# Solved on 7th of February, 2026
class Solution:
    def finalElement(self, nums: list[int]) -> int:
        """
        Calculates the final element remaining after performing subarray deletions.

        :param nums: A list of integers representing the initial array.
        :return: The maximum value between the first and the last element of the array.
        """
        return max(nums[0], nums[-1])