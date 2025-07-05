# Leetcode 1394: Find Lucky Integer in an Array
# https://leetcode.com/problems/find-lucky-integer-in-an-array/
# Solved on 5th of July, 2025
import collections


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        """
        Finds a "lucky number" in an array. A lucky number is an integer
        whose frequency in the array is equal to its value. If there are
        multiple lucky numbers, return the largest one. If no lucky number
        is found, return -1.

        Args:
            arr: A list of integers.
        Returns:
            The largest lucky number, or -1 if none exists.
        """
        # Count frequencies of each number
        freq = collections.Counter(arr)

        # Track the largest number whose frequency equals itself
        res = -1
        for num, count in freq.items():
            if num == count and num > res:
                res = num

        return res