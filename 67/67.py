# Leetcode 67: Add Binary
# https://leetcode.com/problems/add-binary/
# Solved on 15th of February, 2026
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Adds two binary strings and returns their sum as a binary string.

        :param a: The first binary string.
        :param b: The second binary string.
        :return: The sum of a and b as a binary string.
        """
        resultList = []
        indexA = len(a) - 1
        indexB = len(b) - 1
        carryValue = 0

        while indexA >= 0 or indexB >= 0 or carryValue:
            currentSum = carryValue
            if indexA >= 0:
                currentSum += int(a[indexA])
                indexA -= 1
            if indexB >= 0:
                currentSum += int(b[indexB])
                indexB -= 1

            resultList.append(str(currentSum % 2))
            carryValue = currentSum // 2

        return "".join(resultList[::-1])