# Leetcode 1432: Max Difference You Can Get From Changing an Integer
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
# Solved on 15th of June, 2025

class Solution:
    def maxDiff(self, num: int) -> int:
        """
        Given an integer num, you will apply the following two operations to get two integers a and b.
        First, choose a digit x (0-9).
        Second, change all occurrences of x in the decimal representation of num to a digit y (0-9).
        The resulting number is a.
        First, choose a digit x (0-9).
        Second, change all occurrences of x in the decimal representation of num to a digit y (0-9).
        The resulting number is b.
        Return the maximum difference between a and b.
        """
        sNum = str(num)
        aStr = ""
        bStr = ""

        digitToChangeA = ''
        for digit in sNum:
            if digit != '9':
                digitToChangeA = digit
                break

        if digitToChangeA == '':
            aStr = sNum
        else:
            aStr = sNum.replace(digitToChangeA, '9')

        if sNum[0] != '1':
            digitToChangeB = sNum[0]
            bStr = sNum.replace(digitToChangeB, '1')
        else:
            digitToChangeB = ''
            for i in range(1, len(sNum)):
                if sNum[i] not in ['0', '1']:
                    digitToChangeB = sNum[i]
                    break

            if digitToChangeB == '':
                bStr = sNum
            else:
                bStr = sNum.replace(digitToChangeB, '0')

        return int(aStr) - int(bStr)