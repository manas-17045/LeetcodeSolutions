# Leetcode 1837: Sum of Digits in Base K
# https://leetcode.com/problems/sum-of-digits-in-base-k/

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        """
        Calculate the sum of the digits of an integer `n` after it has been converted to
        a base `k` representation. The function iteratively reduces `n` by dividing
        it by `k`, extracting its least significant digit (remainder), and then summing
        these digits until `n` becomes zero.

        This allows the representation and summing of digits of a number in any base `k`.

        :param n: An integer (`n`) that will be converted to base `k` and whose base `k`
            digits will be summed.
        :param k: An integer representing the base in which the integer `n` will
            be represented. Must be greater than 1.
        :return: The sum of the digits of `n` in its base `k` representation.
        :rtype: int
        """
        # Initialize the sum of digits.
        digit_sum = 0

        # Continue the process as long as the number is greater than 0
        while n > 0:
            # The remainder when n is divided by k gives the least significant digit
            # in the current base k representation of n.
            remainder = n % k

            # Add this digit (which is treated as a base 10 number) to the sum.
            digit_sum += remainder

            # Integer divide n by k to move to the next digit.
            # This effectively removes the last digit we just processed.
            n //= k

        # Once n becomes 0, all digits have been extracted and summed.
        return digit_sum