# Leetcode 3012: Minimize Length of Array Using Operations
# https://leetcode.com/problems/minimize-length-of-array-using-operations/
# Solved on 20th of December, 2024
from collections import Counter


class Solution:
    def minimumArrayLength(self, nums: list[int]) -> int:
        """
        Minimizes the length of the array using specific operations.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The minimum possible length of the array.
        """
        min_num = min(nums)
        if any(num % min_num > 0 for num in nums):
            return 1
        
        freq = Counter(nums)[min_num]

        return (freq + 1) // 2