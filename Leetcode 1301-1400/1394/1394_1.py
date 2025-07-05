# Leetcode 1394: Find Lucky Integer in an Array
# https://leetcode.com/problems/find-lucky-integer-in-an-array/
# Solved on 5th of July, 2025
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        """
        Finds a "lucky integer" in the given array.
        A lucky integer is an integer whose frequency in the array is equal to its value.
        If there are multiple lucky integers, return the largest one.
        If there is no lucky integer, return -1.

        :param arr: The input list of integers.
        :return: The largest lucky integer, or -1 if none exists.
        """
        frequencyCounts = [0] * 501

        for number in arr:
            frequencyCounts[number] += 1

        for i in range(500, 0, -1):
            if frequencyCounts[i] == i:
                return i

        return -1