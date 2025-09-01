# Leetcode 1356: Sort Integers by The Number of 1 Bits
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
# Solved on 1st of September, 2025
class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        """
        Sorts an array of integers based on the number of set bits in their binary representation.
        If two numbers have the same number of set bits, they are sorted in ascending order.
        :param arr: A list of integers to be sorted.
        :return: A new list with the integers sorted according to the specified criteria.
        """
        sortedArr = sorted(arr, key=lambda num: (bin(num).count('1'), num))
        return sortedArr