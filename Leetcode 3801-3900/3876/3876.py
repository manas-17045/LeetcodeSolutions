# Leetcode 3876: Construct Uniform Parity Array II
# https://leetcode.com/problems/construct-uniform-parity-array-ii/
# Solved on 29th of March, 2026
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        """
        Determines if a uniform parity array can be constructed based on the minimum values.

        :param nums1: A list of integers to evaluate.
        :return: True if the minimum odd number is less than the minimum even number or if one parity is missing, False otherwise.
        """
        minOdd = float('inf')
        minEven = float('inf')

        for num in nums1:
            if num % 2 != 0:
                if num < minOdd:
                    minOdd = num
            else:
                if num < minEven:
                    minEven = num

        return minOdd == float('inf') or minEven == float('inf') or minOdd < minEven