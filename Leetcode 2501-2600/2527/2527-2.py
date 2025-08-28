# Leetcode 2527: Find Xor-Beauty of Array
# https://leetcode.com/problems/find-xor-beauty-of-array/
# Solved on 28th of August, 2025
class Solution:
    def xorBeauty(self, nums: list[int]) -> int:
        """
        Calculates the XOR beauty of an array.
        :param nums: A list of integers.
        :return: The XOR sum of all elements in the input list.
        """
        res = 0
        for x in nums:
            res ^= x
        return res