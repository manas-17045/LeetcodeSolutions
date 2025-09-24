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
        # Handle zero numerator quickly
        if numerator == 0:
            return "0"

        res = []

        # Determine sign
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        # Work with absolute values to simplify logic
        num = abs(numerator)
        den = abs(denominator)

        # Integer part
        integer_part = num // den
        res.append(str(integer_part))

        # Remainder after integer division
        remainder = num % den
        if remainder == 0:
            return "".join(res)

        # Fractional part exists
        res.append('.')

        # Map remainder -> index in res where the digit for this remainder will be place
        seen = {}

        # Perform long division until remainder becomes 0 or we discover a repeating remainder
        while remainder != 0:
            if remainder in seen:
                # Inset '(' at the first occurrence index and append ')'
                insert_index = seen[remainder]
                res.insert(insert_index, '(')
                res.append(')')
                break

            # Record the position where the next digit (for this remainder) will be placed
            seen[remainder] = len(res)

            remainder *= 10
            digit = remainder // den
            res.append(str(digit))
            remainder %= den

        return "".join(res)