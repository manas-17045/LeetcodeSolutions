# Leetcode 3932: Count K-th Roots in a Range
# https://leetcode.com/problems/count-k-th-roots-in-a-range/
# Solved on 31st of May, 2026
class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        """
        Calculates the number of integers x such that l <= x^k <= r.

        :param l: The lower bound of the range (inclusive).
        :param r: The upper bound of the range (inclusive).
        :param k: The power to which the roots are raised.
        :return: The count of integers whose k-th power falls within [l, r].
        """
        if k == 1:
            return r - l + 1

        def getMaxRoot(targetValue: int) -> int:

            if targetValue < 0:
                return -1

            lowVal = 0
            highVal = 31625
            bestRoot = 0

            while lowVal <= highVal:
                midVal = (lowVal + highVal) // 2
                if midVal ** k <= targetValue:
                    bestRoot = midVal
                    lowVal = midVal + 1
                else:
                    highVal = midVal - 1

            return bestRoot

        return (getMaxRoot(r) + 1) - (getMaxRoot(l - 1) + 1)