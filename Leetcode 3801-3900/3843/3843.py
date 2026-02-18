# Leetcode 3843: First Element with Unique Frequency
# https://leetcode.com/problems/first-element-with-unique-frequency/
# Solved on 18th of February, 2026
class Solution:
    def firstUniqueFreq(self, nums: list[int]) -> int:
        """
        Finds the first element in the list that has a frequency occurring only once among all frequencies.

        :param nums: A list of integers to analyze.
        :return: The first integer with a unique frequency, or -1 if no such integer exists.
        """
        numberFrequency = {}
        for num in nums:
            numberFrequency[num] = numberFrequency.get(num, 0) + 1

        frequencyCount = {}
        for freq in numberFrequency.values():
            frequencyCount[freq] = frequencyCount.get(freq, 0) + 1

        for num in nums:
            currentFreq = numberFrequency[num]
            if frequencyCount[currentFreq] == 1:
                return num

        return -1