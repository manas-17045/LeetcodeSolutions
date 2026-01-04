# Leetcode 3091: Apply Operations to Make Sum of Array Greater Than or Equal to k
# https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/
# Solved on 4th of January, 2026
class Solution:
    def minOperations(self, k: int) -> int:
        """
        Calculates the minimum number of operations to make the sum of an array
        greater than or equal to k.

        :param k: The target sum.
        :return: The minimum number of operations.
        """
        minOps = k
        limit = int(k ** 0.5) + 2
        for value in range(1, limit):
            numElements = (k + value - 1) // value
            currentOps = (value - 1) + (numElements - 1)

            if currentOps < minOps:
                minOps = currentOps

        return minOps