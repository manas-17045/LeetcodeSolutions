# Leetcode 4021: Minimum Operations to Make a Rotated Palindrome I
# https://leetcode.com/problems/minimum-operations-to-make-a-rotated-palindrome-i/
# Solved on 12th of September, 2026
class Solution:
    def minOperations(self, s: str) -> int:
        """
        Calculates the minimum number of operations to make the string a palindrome
        using left rotations and character increments.

        Parameters:
            s (str): The input string consisting of lowercase English letters.

        Returns:
            int: The minimum operations required.
        """
        stringLength = len(s)
        halfLength = stringLength // 2
        charCodes = [ord(charElement) - 97 for charElement in s]
        charCodes = charCodes + charCodes
        minTotalOps = float("inf")

        for rotationCount in range(stringLength):
            if rotationCount >= minTotalOps:
                break

            currentOperations = rotationCount

            for pairIndex in range(halfLength):
                leftIndex = rotationCount + pairIndex
                rightIndex = rotationCount + stringLength - 1 - pairIndex
                charDifference = abs(charCodes[leftIndex] - charCodes[rightIndex])
                stepCost = charDifference if charDifference <= 13 else 26 - charDifference
                currentOperations += stepCost

                if currentOperations >= minTotalOps:
                    break

            if currentOperations < minTotalOps:
                minTotalOps = currentOperations

        return minTotalOps