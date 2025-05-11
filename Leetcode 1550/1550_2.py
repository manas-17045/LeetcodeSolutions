# Leetcode 1550: Three Consecutive Odds
# https://leetcode.com/problems/three-consecutive-odds/

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        """
        Checks if there are three consecutive odd numbers in the given list.

        This function iterates through the input list and checks if any three
        consecutive elements are odd. If such a sequence is found, the
        function returns True. Otherwise, it returns False.

        :param arr: A list of integers to be analyzed.
        :type arr: list[int]
        :return: True if there are three consecutive odd numbers in the list,
            False otherwise.
        :rtype: bool
        """
        for i in range(len(arr) - 2):
            if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
                return True
        return False