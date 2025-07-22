# Leetcode 1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# Solved on 22nd of July, 2025
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        """
        Calculates the number of sub-arrays of size k whose average is greater than or equal to threshold.
        Args:
            arr (list[int]): The input array of integers.
            k (int): The desired size of the sub-arrays.
            threshold (int): The minimum average value for a sub-array to be counted.
        Returns:
            int: The number of sub-arrays meeting the criteria.
        """
        resultCount = 0
        windowSum = 0
        windowStart = 0
        targetSum = k * threshold

        for windowEnd in range(len(arr)):
            windowSum += arr[windowEnd]

            windowSize = windowEnd - windowStart + 1
            if windowSize == k:
                if windowSum >= targetSum:
                    resultCount += 1
                windowSum -= arr[windowStart]
                windowStart += 1

        return resultCount