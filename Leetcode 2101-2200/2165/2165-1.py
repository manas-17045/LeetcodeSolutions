# Leetcode 2165: Smallest Value of the Rearranged Number
# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
# Solved on 4th of September, 2025
class Solution:
    def smallestNumber(self, num: int) -> int:
        """
        Rearranges the digits of a given number to form the smallest possible number.

        Args:
            num (int): The input integer.
        Returns:
            int: The smallest number formed by rearranging the digits of `num`.
        """
        if num == 0:
            return 0

        isNegative = num < 0
        numStr = str(abs(num))
        digits = sorted(list(numStr))

        if isNegative:
            resultStr = "".join(reversed(digits))
            return -int(resultStr)
        else:
            if digits[0] == '0':
                firstNonZeroIndex = 0
                for i in range(len(digits)):
                    if digits[i] != '0':
                        firstNonZeroIndex = i
                        break
                digits[0], digits[firstNonZeroIndex] = digits[firstNonZeroIndex], digits[0]

            resultStr = "".join(digits)
            return int(resultStr)