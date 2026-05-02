# Leetcode 788: Rotated Digits
# https://leetcode.com/rotated-digits/
# Solved on 2nd of May, 2026
class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
        Counts how many numbers from 1 to n are good after rotating each digit by 180 degrees.
        A number is good if it remains a valid number and is different from the original.

        :param n: The upper bound integer (inclusive).
        :return: The total count of good numbers in the range [1, n].
        """
        stateList = [0] * (n + 1)
        validCount = 0

        for currNum in range(n + 1):
            if currNum < 10:
                if currNum in (0, 1, 8):
                    stateList[currNum] = 1
                elif currNum in (2, 5, 6, 9):
                    stateList[currNum] = 2
                    validCount += 1

            else:
                leftPart = stateList[currNum // 10]
                rightPart = stateList[currNum % 10]
                if leftPart == 1 and rightPart == 1:
                    stateList[currNum] = 1
                elif leftPart >= 1 and rightPart >= 1:
                    stateList[currNum] = 2
                    validCount += 1

        return validCount