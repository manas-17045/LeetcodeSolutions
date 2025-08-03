# Leetcode 2439: Minimize Maximum of Array
# https://leetcode.com/problems/minimize-maximum-of-array/
# Solved on 3rd of August, 2025
class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        """
        Calculates the minimum possible maximum value in the array after performing
        any number of operations. An operation consists of decreasing an element
        nums[i] by 1 and increasing nums[i-1] by 1.
        :param nums: A list of integers.
        :return: The minimum possible maximum value in the array.
        """
        prefix_sum = 0
        answer = 0
        for i, v in enumerate(nums):
            prefix_sum += v

            avg_ceil = (prefix_sum + i) // (i + 1)

            if avg_ceil > answer:
                answer = avg_ceil

        return answer