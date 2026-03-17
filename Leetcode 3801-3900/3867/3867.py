# Leetcode 3867: Sum of GCD of Formed Pairs
# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/
# Solved on 17th of March, 2026
import math


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        """
        Calculates the sum of GCDs of pairs formed from a processed list of prefix GCDs.

        :param nums: A list of integers to process.
        :return: The total sum of GCDs of the formed pairs.
        """
        prefixGcd = []
        currentMax = 0
        for num in nums:
            if num > currentMax:
                currentMax = num
            prefixGcd.append(math.gcd(num, currentMax))

        prefixGcd.sort()

        totalSum = 0
        leftIndex = 0
        rightIndex = len(prefixGcd) - 1

        while leftIndex < rightIndex:
            totalSum += math.gcd(prefixGcd[leftIndex], prefixGcd[rightIndex])
            leftIndex += 1
            rightIndex -= 1

        return totalSum