# Leetcode 3463: Check If Digits Are Equal in String After Operations II
# https://leetcode.com/problems/check-if-digits-are-equal-after-operations-ii/
# Solved on 1st of August, 2025
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        """
        Checks if the final digits obtained from two different operations on the input string are equal.

        :param s: The input string consisting of digits.
        :return: True if the final digits are equal, False otherwise.
        """
        n = len(s)
        k = n - 2

        digits = [int(digit) for digit in s]

        cSmallMod5 = [
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 2, 1, 0, 0],
            [1, 3, 3, 1, 0],
            [1, 4, 1, 4, 1]
        ]

        crtTable = [
            [0, 6, 2, 8, 4],
            [5, 1, 7, 3, 9]
        ]

        def getCombMod5(num, r):
            if r < 0 or r > num:
                return 0
            
            result = 1
            tempNum = num
            tempR = r

            while tempNum > 0:
                numDigit = tempNum % 5
                rDigit = tempR % 5
                result = (result * cSmallMod5[numDigit][rDigit]) % 5
                tempNum //= 5
                tempR //= 5

            return result
        
        finalDigitZero = 0
        finalDigitOne = 0

        for i in range(k + 1):
            cMod2 = 1 if (i % k) == i else 0
            cMod5 = getCombMod5(k, i)
            cMod10 = crtTable[cMod5][cMod5]

            finalDigitZero = (finalDigitZero + cMod10 * digits[i]) % 10
            finalDigitOne = (finalDigitOne + cMod10 * digits[i + 1]) % 10
            
        return finalDigitZero == finalDigitOne