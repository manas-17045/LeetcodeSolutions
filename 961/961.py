# Leetcode 961: N-Repeated Element in Size 2N Array
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# Solved on 2nd of January, 2025
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        """
        Finds the element that appears N times in an array of size 2N.

        :param nums: A list of integers where one element appears N times.
        :return: The element that is repeated N times.
        """
        seenElements = set()

        for element in nums:
            if element in seenElements:
                return element

            seenElements.add(element)