# Leetcode 3689: Maximum Total Subarray Value I
# https://leetcode.com/problems/maximum-total-subarray-value-i/
# Solved on 3rd of November, 2025
class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum total value of a subarray.

        :param nums: A list of integers representing the array.
        :param k: An integer multiplier.
        :return: The maximum total value.
        """
        if not nums:
            return 0

        maxNum = max(nums)
        minNum = min(nums)

        maxSingleValue = maxNum - minNum

        return maxSingleValue * k