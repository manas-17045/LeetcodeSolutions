# Leetcode 1481: Least Number of Unique Integers after K Removals
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
# Solved on 10th of November, 2025
import collections


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        """
        Given an array of integers arr and an integer k, return the least number of unique integers
        after removing exactly k elements.

        :param arr: A list of integers.
        :param k: The number of elements to remove.
        :return: The least number of unique integers after removing k elements.
        """
        freqMap = collections.Counter(arr)

        frequencies = sorted(freqMap.values())

        uniqueCount = len(frequencies)

        for freq in frequencies:
            if k >= freq:
                k -= freq
                uniqueCount -= 1
            else:
                break

        return uniqueCount