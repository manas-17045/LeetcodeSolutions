# Leetcode 3371: Identify the Largest Outlier in an Array
# https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/
# Solved on 24th of November, 2025
class Solution:
    def getLargestOutlier(self, nums: list[int]) -> int:
        """
        Identifies the largest outlier in an array. An outlier `x` is defined such that
        the sum of the remaining elements `(totalSum - x)` can be split into two equal halves.

        :param nums: A list of integers.
        :return: The largest integer `x` from `nums` that satisfies the outlier condition.
        """
        totalSum = sum(nums)
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        maxOutlier = -float('inf')

        for num in counts:
            remainingSum = totalSum - num
            if remainingSum % 2 == 0:
                target = remainingSum // 2
                if target in counts:
                    if target != num or counts[target] > 1:
                        if num > maxOutlier:
                            maxOutlier = num

        return maxOutlier