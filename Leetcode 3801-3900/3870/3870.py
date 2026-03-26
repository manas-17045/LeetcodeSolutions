# Leetcode 3870: Count Commas in Range
# https://leetcode.com/problems/count-commas-in-range/
# Solved on 26th of March, 2026
class Solution:
    def countCommas(self, n: int) -> int:
        """
        Calculates the total number of commas used when writing all integers from 1 to n.

        :param n: The upper limit of the range (inclusive).
        :return: The total count of commas in the representation of numbers from 1 to n.
        """
        totalCommas = 0
        threshold = 1000

        while n >= threshold:
            totalCommas += n - threshold + 1
            threshold *= 1000

        return totalCommas