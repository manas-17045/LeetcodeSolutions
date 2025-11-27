# Leetcode 1551: Minimum Operations to Make Array Equal
# https://leetcode.com/problems/minimum-operations-to-make-array-equal/
# Solved on 27th of November, 2025
class Solution:
    def minOperations(self, n: int) -> int:
        """
        Calculates the minimum number of operations required to make all elements of an array equal.
        The array is initially defined such that arr[i] = (2 * i) + 1.

        :param n: The length of the array.
        :return: The minimum number of operations.
        """
        return n * n // 4