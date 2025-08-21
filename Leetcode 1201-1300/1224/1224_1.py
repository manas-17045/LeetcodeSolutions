# Leetcode 1224: Maximum Equal Frequency
# https://leetcode.com/problems/maximum-equal-frequency/
# Solved on 21st of August, 2025
class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        """
        Finds the maximum length of a prefix of the given array such that after removing exactly one element from it,
        all remaining elements have the same frequency.

        Args:
            nums (list[int]): A list of integers.
        Returns:
            int: The maximum length of a valid prefix.
        """
        numCounts = {}
        freqCounts = {}
        maxLength = 0

        for i, currentNum in enumerate(nums):
            previousCount = numCounts.get(currentNum, 0)
            numCounts[currentNum] = previousCount + 1
            currentCount = previousCount + 1

            if previousCount > 0:
                freqCounts[previousCount] -= 1
                if freqCounts[previousCount] == 0:
                    del freqCounts[previousCount]

            freqCounts[currentCount] = freqCounts.get(currentCount, 0) + 1

            isValid = False
            if len(freqCounts) == 1:
                freq, countOfFreq = next(iter(freqCounts.items()))
                if freq == 1 or countOfFreq == 1:
                    isValid = True
            elif len(freqCounts) == 2:
                (freq1, count1), (freq2, count2) = freqCounts.items()

                if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
                    isValid = True
                elif (freq1 + 1 == freq2 and count2 == 1) or (freq2 + 1 == freq1 and count1 == 1):
                    isValid = True

            if isValid:
                maxLength = i + 1

        return maxLength