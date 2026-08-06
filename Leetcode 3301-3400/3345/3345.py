# Leetcode 3345: Smallest Divisible Digit Product I
# https://leetcode.com/problems/smallest-divisible-digit-product-i/
# Solved on 6th of August, 2026
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        """
        Finds the smallest number greater than or equal to n whose digit product is divisible by t.

        :param n: The lower bound of the range.
        :param t: The divisor.
        :return: The smallest number in the range [n, infinity) whose digit product is divisible by t.
        """
        currentNum = n
        while True:
            if self.getDigitProduct(currentNum) % t == 0:
                return currentNum
            
            currentNum += 1

    def getDigitProduct(self, currentVal: int) -> int:
        digitProduct = 1
        while currentVal > 0:
            digitProduct *= currentVal % 10
            currentVal //= 10
        
        return digitProduct