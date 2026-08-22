# Leetcod 3622: Check Divisibility by Digit Sum and Product
# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
# Solved on 22nd of August, 2026
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        """
        Checks if a given integer n is divisible by the sum of its digits plus the
        product of its digits.

        @param n: The integer to check for divisibility.
        @return: true if n is divisible by the sum of its digits plus the product of
                 its digits, false otherwise.
        """
        digitSum = 0
        digitProduct = 1
        tempVal = n

        while tempVal > 0:
            currentdigit = tempVal % 10
            digitSum += currentdigit
            digitProduct *= currentdigit
            tempVal //= 10

        totalSum = digitSum + digitProduct
        return n % totalSum == 0