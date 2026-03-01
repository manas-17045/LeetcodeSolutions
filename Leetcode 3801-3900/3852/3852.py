# Leetcode 3852: Smallest Pair With Different Frequencies
# https://leetcode.com/problems/smallest-pair-with-different-frequencies/
# Solved on 1st of March, 2026
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        """
        Finds the lexicographically smallest pair of numbers with different frequencies.

        Args:
            nums (list[int]): A list of integers.

        Returns:
            list[int]: The smallest pair [valX, valY] with different frequencies, or [-1, -1] if none exist.
        """
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        sortedUniqueNums = sorted(freqMap.keys())

        for i in range(len(sortedUniqueNums)):
            for j in range(i + 1, len(sortedUniqueNums)):
                valX = sortedUniqueNums[i]
                valY = sortedUniqueNums[j]

                if freqMap[valX] != freqMap[valY]:
                    return [valX, valY]

        return [-1, -1]