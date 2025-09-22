# Leetcode 3005: Count Elements With Maximum Frequency
# https://leetcode.com/problems/count-elements-with-maximum-frequency/
# Resolved on 22nd of September, 2025
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        """
        Calculates the total frequency of elements that appear with the maximum frequency in the given list.
        :param nums: A list of integers.
        :return: The sum of frequencies of all elements that have the maximum frequency.
        """
        counts = {}
        maxFreq = 0
        sum_max = 0

        for x in nums:
            c = counts.get(x, 0) + 1
            counts[x] = c

            if c > maxFreq:
                maxFreq = c
                sum_max = c
            elif c == maxFreq:
                sum_max += c

        return sum_max