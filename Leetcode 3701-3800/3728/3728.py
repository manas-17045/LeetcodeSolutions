# Leetcode 3728: Stable Subarrays With Equal Boundary and Interior Sum
# https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/
# Solved on 27th of December, 2025
from collections import defaultdict


class Solution:
    def countStableSubarrays(self, capacity: list[int]) -> int:
        """
        Counts the number of stable subarrays in the given capacity array.
        A subarray is stable if its boundary sum equals its interior sum.

        Args:
            capacity: A list of integers representing the capacities.
        Returns:
            The total count of stable subarrays.
        """
        n = len(capacity)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + capacity[i]

        frequencyMap = defaultdict(int)
        stableSubarraysCount = 0

        for i in range(n):
            if i >= 2:
                leftIndex = i - 2
                key = (capacity[leftIndex], prefixSum[leftIndex])
                frequencyMap[key] += 1

            targetPrefix = prefixSum[i] - 2 * capacity[i]
            queryKey = (capacity[i], targetPrefix)
            stableSubarraysCount += frequencyMap[queryKey]

        return stableSubarraysCount