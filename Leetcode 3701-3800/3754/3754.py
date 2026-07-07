# Leetcode 3754: Concatenate Non-Zero Digits and Multiply by Sum I
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
# Solved on 7th of July, 2026
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        """
        Concatenates the non-zero digits of a number and multiplies the result by
        the sum of the non-zero digits.
        
        @param n: The number to process.
        @return: The result of concatenating the non-zero digits and multiplying by the sum of the non-zero digits.
        """
        digitsStr = "".join(eachDigit for eachDigit in str(n) if eachDigit != '0')
        if not digitsStr:
            return 0

        targetValue = int(digitsStr)
        digitSum = sum(int(eachDigit) for eachDigit in digitsStr)

        return targetValue * digitSum