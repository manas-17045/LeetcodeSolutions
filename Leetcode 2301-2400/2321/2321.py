# Leetcode 2321: Maximum Score of Spliced Array
# https://leetcode.com/problems/maximum-score-of-spliced-array/
# Solved on 5th of November, 2025
class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the maximum possible score of a spliced array.

        Args:
            nums1: A list of integers representing the first array.
            nums2: A list of integers representing the second array.
        Returns:
            The maximum score achievable by splicing the arrays.
        """
        n = len(nums1)
        sum1 = 0
        sum2 = 0

        currentMaxGain = 0
        maxGain = 0

        currentMinGain = 0
        minGain = 0

        for i in range(n):
            sum1 += nums1[i]
            sum2 += nums2[i]

            diff = nums2[i] - nums1[i]

            currentMaxGain += diff
            if currentMaxGain < 0:
                currentMaxGain = 0
            if maxGain < currentMaxGain:
                maxGain = currentMaxGain

            currentMinGain += diff
            if currentMinGain > 0:
                currentMinGain = 0
            if minGain > currentMinGain:
                minGain = currentMinGain

        ans1 = sum1 + maxGain
        ans2 = sum2 - minGain

        return max(ans1, ans2)