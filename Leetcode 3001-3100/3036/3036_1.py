# Leetcode 3036: Number of Subarrays That match a Pattern II
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/
# Solved on 8th of June, 2025

class Solution:
    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        """
        Counts the number of subarrays in nums that match the given pattern.

        Args:
            nums: A list of integers.
            pattern: A list of integers representing the pattern to match.
                     1 means increasing, 0 means equal, -1 means decreasing.

        Returns:
            The number of matching subarrays.
        """
        n = len(nums)
        m = len(pattern)

        relations = [(nums[i + 1] > nums[i]) - (nums[i + 1] < nums[i]) for i in range(n - 1)]

        lpsArray = [0] * m
        prevLpsLength = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[prevLpsLength]:
                prevLpsLength += 1
                lpsArray[i] = prevLpsLength
                i += 1
            else:
                if prevLpsLength != 0:
                    prevLpsLength = lpsArray[prevLpsLength - 1]
                else:
                    lpsArray[i] = 0
                    i += 1

        matchCount = 0
        textIndex = 0
        patternIndex = 0
        relationsSize = n - 1

        while textIndex < relationsSize:
            if pattern[patternIndex] == relations[textIndex]:
                patternIndex += 1
                textIndex += 1

            if patternIndex == m:
                matchCount += 1
                patternIndex = lpsArray[patternIndex - 1]
            elif textIndex < relationsSize and pattern[patternIndex] != relations[textIndex]:
                if patternIndex != 0:
                    patternIndex = lpsArray[patternIndex - 1]
                else:
                    textIndex += 1

        return matchCount