# Leetcode 3005: Count Elements With Maximum Frequency
# https://leetcode.com/problems/count-elements-with-maximum-frequency/
# Resolved on 22nd of September, 2025
import collections


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        """
        Counts the total occurrences of elements that have the maximum frequency.

        :param nums: A list of integers.
        :return: The sum of frequencies of all elements that appear with the maximum frequency.
        """

        frequencyMap = collections.defaultdict(int)
        maxFrequency = 0
        totalFrequencies = 0

        for num in nums:
            frequencyMap[num] += 1
            currentFrequency = frequencyMap[num]

            if currentFrequency > maxFrequency:
                maxFrequency = currentFrequency
                totalFrequencies = currentFrequency
            elif currentFrequency == maxFrequency:
                totalFrequencies += maxFrequency

        return totalFrequencies