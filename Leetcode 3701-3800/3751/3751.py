# Leetcode 3751: Total Waviness of Numbers in Range I
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/
# Solved on 26th of December, 2025
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        """
        Calculates the total waviness of numbers within a given range [num1, num2].
        A number's waviness is determined by digits that are either strictly greater
        or strictly smaller than both their immediate neighbors.
        :param num1: The starting number of the range (inclusive).
        :param num2: The ending number of the range (inclusive).
        :return: The total waviness count for all numbers in the range.
        """
        totalWaviness = 0

        for currentNum in range(num1, num2 + 1):
            if currentNum < 100:
                continue

            numStr = str(currentNum)
            strLen = len(numStr)
            for i in range(1, strLen - 1):
                currChar = numStr[i]
                prevChar = numStr[i - 1]
                nextChar = numStr[i + 1]

                if currChar > prevChar and currChar > nextChar:
                    totalWaviness += 1
                elif currChar < prevChar and currChar < nextChar:
                    totalWaviness += 1

        return totalWaviness