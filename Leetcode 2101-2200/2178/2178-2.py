# Leetcode 2178: Maximum Split of Positive Even Integers
# https://leetcode.com/problems/maximum-split-of-positive-even-integers/
# Solved on 4th of September, 2025
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        """
        Splits a given even integer `finalSum` into the maximum number of unique positive even integers.
        :param finalSum: The integer to be split.
        :return: A list of unique positive even integers that sum up to `finalSum`, or an empty list if `finalSum` is odd.
        """
        if finalSum % 2:
            return []

        res = []
        cur = 2

        # Take smallest unused evens while possible
        while finalSum >= cur:
            res.append(cur)
            finalSum -= cur
            cur += 2

        # If some leftover remains, add it to the last element
        if finalSum > 0:
            res[-1] += finalSum
        return res