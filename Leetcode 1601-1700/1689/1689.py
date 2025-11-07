# Leetcode 1689: Partitioning Into Minimum Number of Deci-Binary Numbers
# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# Solved on 7th of November, 2025
class Solution:
    def minPartitions(self, n: str) -> int:
        """
        Calculates the minimum number of deci-binary numbers needed to sum up to the given string 'n'.

        :param n: A string representing a positive integer.
        :return: The minimum number of deci-binary numbers.
        """
        maxDigit = 0
        for digitChar in n:
            digitValue = int(digitChar)
            if digitValue > maxDigit:
                maxDigit = digitValue
                if maxDigit == 9:
                    break

        return maxDigit