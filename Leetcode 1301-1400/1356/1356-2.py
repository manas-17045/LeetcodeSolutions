# Leetcode 1356: Sort Integers by The Number of 1 Bits
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
# Solved on 1st of September, 2025
class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        """
        Sorts an array of integers based on the number of set bits (1s in their binary representation)
        in ascending order. If two numbers have the same number of set bits, they are then sorted
        in ascending numerical order.
        :param arr: A list of integers to be sorted.
        :return: A new list containing the sorted integers.
        """
        if hasattr(int, "bit_count"):
            popCount = int.bit_count
        else:
            popCount = lambda x: bin(x).count("1")

        # Sort by tuple
        return sorted(arr, key=lambda x: (popCount(x), x))