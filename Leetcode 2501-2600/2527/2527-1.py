# Leetcode 2527: Find Xor-Beauty of Array
# https://leetcode.com/problems/find-xor-beauty-of-array/
# Solved on 28th of August, 2025
class Solution:
    def xorBeauty(self, nums: list[int]) -> int:
        """
        Calculates the XOR-beauty of the given array.
        The XOR-beauty of an array is defined as the XOR sum of all its elements.

        :param nums: A list of integers.
        :return: The XOR-beauty of the array.
        """
        xorSum = 0
        for num in nums:
            xorSum ^= num
        return xorSum