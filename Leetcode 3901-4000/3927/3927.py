# Leetcode 3927: Minimize Array Sum Using Divisible Replacements
# https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/
# Solved on 26th of May, 2026
class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        """
        Calculates the minimum possible sum of the array by replacing each element
        with its smallest divisor present in the array.

        :param nums: List of integers to be processed.
        :return: The minimized sum of the array after replacements.
        """
        maxVal = max(nums)
        minReplacement = list(range(maxVal + 1))
        sortedNums = sorted(set(nums))

        for num in sortedNums:
            if minReplacement[num] == num:
                for multiple in range(num, maxVal + 1, num):
                    if minReplacement[multiple] == multiple:
                        minReplacement[multiple] = num

        totalSum = 0
        for num in nums:
            totalSum += minReplacement[num]

        return totalSum