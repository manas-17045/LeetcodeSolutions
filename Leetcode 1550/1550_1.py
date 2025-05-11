# Leetcode 1550: Three Consecutive Odds
# https://leetcode.com/problems/three-consecutive-odds/

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        """
        Given an integer array arr, return true if there are three consecutive odd numbers in the array.
        Otherwise, return false.

        :param arr: A list of integers
        :return: True if there are three consecutive odd numbers, False otherwise.
        """
        count = 0
        for a in arr:
            count += 1 if a % 2 == 1 else 0
            if count == 3:
                return True
        return False