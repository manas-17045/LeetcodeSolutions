# Leetcode 2808: Minimum Seconds to Equalize a Circular Array
# https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/
# Solved on 1st of December, 2025
class Solution:
    def minimumSeconds(self, nums: list[int]) -> int:
        """
        Calculates the minimum seconds required to equalize a circular array.

        Args:
            nums: A list of integers representing the circular array.

        Returns:
            The minimum number of seconds to make all elements in the array equal.

        """
        n = len(nums)
        indexMap = {}

        for i, value in enumerate(nums):
            if value not in indexMap:
                indexMap[value] = []
            indexMap[value].append(i)

        minSeconds = n

        for indices in indexMap.values():
            indices.append(indices[0] + n)
            maxGap = 0

            for i in range(len(indices) - 1):
                gap = indices[i + 1] - indices[i]
                if gap > maxGap:
                    maxGap = gap

            seconds = maxGap // 2
            if seconds < minSeconds:
                minSeconds = seconds

        return minSeconds