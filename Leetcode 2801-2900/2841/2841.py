# Leetcode 2841: Maximum Sum of Almost Unique Subarray
# https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/
# Solved on 1st of November, 2025
class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        """
        Calculates the maximum sum of an "almost unique" subarray of length k.
        An "almost unique" subarray is defined as a subarray that has at least m distinct elements.

        Args:
            nums (list[int]): The input list of integers.
            m (int): The minimum number of distinct elements required for an "almost unique" subarray.
            k (int): The fixed length of the subarrays to consider.
        Returns:
            int: The maximum sum found among all "almost unique" subarrays of length k.
        """
        maxSum = 0
        currentSum = 0
        freqMap = {}
        left = 0

        for right in range(len(nums)):
            numRight = nums[right]
            currentSum += numRight
            freqMap[numRight] = freqMap.get(numRight, 0) + 1

            windowSize = right - left + 1

            if windowSize == k:
                if len(freqMap) >= m:
                    maxSum = max(maxSum, currentSum)

                numLeft = nums[left]
                currentSum -= numLeft
                freqMap[numLeft] -= 1

                if freqMap[numLeft] == 0:
                    del freqMap[numLeft]

                left += 1

        return maxSum