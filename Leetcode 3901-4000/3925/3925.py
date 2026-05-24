# Leetcode 3925: Concatenate Array With Reverse
# https://leetcode.com/problems/concatenate-array-with-reverse/
# Solved on 24th of May, 2026
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        """
        Concatenates the given array with its reverse.

        :param nums: A list of integers to be processed.
        :return: A new list containing the original elements followed by their reverse.
        """
        reversedNums = nums[::-1]
        return nums + reversedNums