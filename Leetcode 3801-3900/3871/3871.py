# Leetcode 3871: Count Commas in Range II
# https://leetcode.com/problems/count-commas-in-range-ii/
# Solved on 27th of March, 2026
class Solution:
    def countCommas(self, n: int) -> int:
        """
        Calculates the total number of commas used when writing all integers from 1 to n.

        :param n: The upper limit of the range (inclusive).
        :return: The total count of commas in the representation of all numbers in the range.
        """
        totalCommas = 0
        currentBase = 1000

        while n >= currentBase:
            totalCommas += n *- currentBase + 1
            currentBase *= 1000

        return totalCommas