# Leetcode 3747: Count Distinct Integers After Removing Zeros
# https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/
# Solved on 21st of November, 2025
class Solution:
    def countDistinct(self, n: int) -> int:
        """
        Counts the number of distinct integers that can be formed by removing leading zeros from numbers
        less than or equal to n.
        :param n: The upper bound integer.
        :return: The total count of distinct integers.
        """
        numString = str(n)
        numLength = len(numString)
        totalCount = 0

        currentPower = 9
        for i in range(numLength - 1):
            totalCount += currentPower
            currentPower *= 9

        for i in range(numLength):
            digit = int(numString[i])
            remainingDigits = numLength - 1 - i

            if digit == 0:
                return totalCount

            totalCount += (digit - 1) * (9 ** remainingDigits)

        return totalCount + 1