# Leetcode 1567: Maximum Length of Subarray With Positive Product
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
# Solved on 10th of September, 2025
class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        """
        Calculates the maximum length of a subarray with a positive product.

        :param nums: A list of integers.
        :return: The maximum length of a subarray with a positive product.
        """
        maxLength = 0
        positiveLength = 0
        negativeLength = 0

        for num in nums:
            if num == 0:
                positiveLength = 0
                negativeLength = 0
            elif num > 0:
                positiveLength = positiveLength + 1
                if negativeLength > 0:
                    negativeLength = negativeLength + 1
            else:
                oldPositiveLength = positiveLength
                if negativeLength > 0:
                    positiveLength = negativeLength + 1
                else:
                    positiveLength = 0
                negativeLength = oldPositiveLength + 1

            if positiveLength > maxLength:
                maxLength = positiveLength

        return maxLength