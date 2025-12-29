# Leetcode 3628: Maximum Number of Subsequences After One Inserting
# https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/
# Solved on 29th of December, 2025
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        """
        Calculates the maximum number of subsequences "LCT" that can be formed after inserting one character
        ('L', 'C', or 'T') into the given string `s`.

        Args:
            s (str): The input string consisting of characters 'L', 'C', and 'T'.

        Returns:
            int: The maximum number of subsequences "LCT" after one insertion.
        """
        tCount = 0
        ctCount = 0
        for char in reversed(s):
            if char == 'T':
                tCount += 1
            elif char == 'C':
                ctCount += tCount

        lCount = 0
        lcCount = 0
        lctCount = 0
        maxCGain = 0

        for char in s:
            currentCGain = lCount * tCount
            if currentCGain > maxCGain:
                maxCGain = currentCGain

            if char == 'L':
                lCount += 1
            elif char == 'C':
                lcCount += lCount
            elif char == 'T':
                lctCount += lcCount
                tCount -= 1

        return lctCount + max(ctCount, lcCount, maxCGain)