# Leetcode 2834: Find the Minimum Possible Sum of a Beautiful Array
# https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/
# Solved on 7th of October, 2025
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        """
        Finds the minimum possible sum of a beautiful array.

        Args:
            n (int): The number of elements in the array.
            target (int): The target sum for pairs.
        Returns:
            int: The minimum possible sum of a beautiful array modulo 10^9 + 7.
        """
        modulo = 1000000007

        def getSumOfRange(start, end):
            if start > end:
                return 0

            startMod = start % modulo
            endMod = end % modulo

            count = end - start + 1
            countMod = count % modulo

            sumOfEnds = (startMod + endMod) % modulo

            totalSum = (countMod * sumOfEnds) % modulo

            modInverseOfTwo = pow(2, modulo - 2, modulo)

            totalSum = (totalSum * modInverseOfTwo) % modulo
            return totalSum

        halfTarget = target // 2

        if n <= halfTarget:
            return getSumOfRange(1, n)
        else:
            firstSum = getSumOfRange(1, halfTarget)

            countRemaining = n - halfTarget

            secondStart = target
            secondEnd = target + countRemaining - 1

            secondSum = getSumOfRange(secondStart, secondEnd)

            return (firstSum + secondSum) % modulo