# Leetcode 1977: Number of Ways to Separate Numbers
# https://leetcode.com/problems/number-of-ways-to-separate-numbers/
# Solved on 22nd of September, 2025
from array import array


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        """
        Calculates the number of ways to separate a given string of digits into a sequence of non-decreasing numbers.

        Args:
            num (str): The input string of digits.
        Returns:
            int: The number of ways to separate the numbers, modulo 10^9 + 7.
        """
        modulo = 10 ** 9 + 7
        numString = num
        numLength = len(numString)

        if numLength == 0 or numString[0] == '0':
            return 0

        longestCommonPrefix = [array('H', [0] * (numLength + 1)) for _ in range(numLength + 1)]
        for firstIndex in range(numLength - 1, -1, -1):
            currentRow = longestCommonPrefix[firstIndex]
            nextRow = longestCommonPrefix[firstIndex + 1]
            for secondIndex in range(numLength - 1, -1, -1):
                if numString[firstIndex] == numString[secondIndex]:
                    currentRow[secondIndex] = nextRow[secondIndex + 1] + 1
                else:
                    currentRow[secondIndex] = 0

        prefixSums = [array('I', [0] * (i + 1)) for i in range(numLength + 1)]

        for prefixLength in range(1, numLength + 1):
            currentPrefixSumRow = prefixSums[prefixLength]
            for lastNumberLength in range(1, prefixLength + 1):
                startIndex = prefixLength - lastNumberLength
                if numString[startIndex] == '0':
                    dpValue = 0
                else:
                    prevPrefixLength = prefixLength - lastNumberLength
                    if prevPrefixLength == 0:
                        dpValue = 1
                    else:
                        maxLength = min(lastNumberLength, prevPrefixLength)
                        totalWays = prefixSums[prevPrefixLength][maxLength]

                        if prevPrefixLength >= lastNumberLength:
                            prevNumberStartIndex = prevPrefixLength - lastNumberLength
                            currentNumberStartIndex = startIndex
                            commonPrefixLen = longestCommonPrefix[prevNumberStartIndex][currentNumberStartIndex]

                            if commonPrefixLen < lastNumberLength and numString[
                                prevNumberStartIndex + commonPrefixLen] > numString[
                                currentNumberStartIndex + commonPrefixLen]:
                                waysWithPrevLength = (prefixSums[prevPrefixLength][lastNumberLength] -
                                                      prefixSums[prevPrefixLength][lastNumberLength - 1]) % modulo
                                totalWays = (totalWays - waysWithPrevLength) % modulo

                        dpValue = totalWays % modulo

                currentPrefixSumRow[lastNumberLength] = (currentPrefixSumRow[lastNumberLength - 1] + dpValue) % modulo

        return prefixSums[numLength][numLength] % modulo