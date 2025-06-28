# Leetcode 2099: Find Subsequence of Length K With the Largest Sum
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
# Solved on 28th of June, 2025
class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        """
        Given an integer array nums and an integer k, return the subsequence of nums of length k that has the largest
        sum. A subsequence is an array that can be derived from another array by deleting some or no elements without
        changing the order of the remaining elements.

        :param nums: The input list of integers.
        :param k: The desired length of the subsequence.
        :return: A list representing the subsequence of length k with the largest sum.
        """
        indexedNums = []
        for index, num in enumerate(nums):
            indexedNums.append((num, index))

        indexedNums.sort(key=lambda p: p[0], reverse=True)

        topK = indexedNums[:k]

        topK.sort(key=lambda p: p[1])

        result = []
        for num, index in topK:
            result.append(num)

        return result