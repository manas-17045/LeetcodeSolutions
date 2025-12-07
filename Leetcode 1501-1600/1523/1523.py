# Leetcode 1523: Count Odd Numbers in an Interval Range
# https://leetcode.com/probelms/count-odd-numbers-in-an-interval-range/
# Solved on 7th of December, 2025
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Counts the number of odd integers within a given interval [low, high].

        :param low: The lower bound of the interval (inclusive).
        :param high: The upper bound of the interval (inclusive).
        :return: The count of odd numbers in the interval.
        """
        return (high - 1) // 2 - low // 2