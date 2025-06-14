# Leetcode 2566: Maximum Difference by Remapping a Digit
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
# Solved on 14th of June, 2025

class Solution:
    def minMaxDifference(self, num: int) -> int:
        """
        Calculates the maximum difference between two numbers obtained by remapping a single digit in the input number.

        To maximize the number, we replace the first digit that is not '9' with '9'.
        To minimize the number, we replace the first digit with '0'.

        Args:
            num: The input integer.
        """
        numStr = str(num)

        maxDigit = ''
        for char in numStr:
            if char != '9':
                maxDigit = char
                break

        if not maxDigit:
            maxDigit = '9'

        maxVal = int(numStr.replace(maxDigit, '9'))

        minDigit = numStr[0]
        minVal = int(numStr.replace(minDigit, '0'))

        return maxVal - minVal