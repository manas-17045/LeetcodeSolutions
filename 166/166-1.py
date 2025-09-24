# Leetcode 166: Fraction to Recurring Decimal
# https://leetcode.com/problems/fraction-to-recurring-decimal/
# Solved on 24th of September, 2025
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        Given two integers representing the numerator and denominator of a fraction, return the fraction as a string.

        If the fractional part is repeating, enclose the repeating part in parentheses.

        :param numerator: The numerator of the fraction.
        :param denominator: The denominator of the fraction.
        :return: The fraction as a string.
        """
        if numerator == 0:
            return "0"

        result = []
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        num = abs(numerator)
        den = abs(denominator)

        result.append(str(num // den))
        remainder = num % den

        if remainder == 0:
            return "".join(result)

        result.append(".")
        remainderMap = {}

        while remainder != 0:
            if remainder in remainderMap:
                result.insert(remainderMap[remainder], "(")
                result.append(")")
                break

            remainderMap[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // den))
            remainder %= den

        return "".join(result)