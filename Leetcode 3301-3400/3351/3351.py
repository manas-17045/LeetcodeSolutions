# Leetcode 3351: Sum of Good Subsequences
# https://leetcode.com/problems/sum-of-good-subsequences/
# Solved on 4th of December, 2025
class Solution:
    def sumOfGoodSubsequences(self, nums: list[int]) -> int:
        """
        Calculates the sum of all "good" subsequences.
        A subsequence is considered "good" if all adjacent elements in the subsequence differ by at most 1.
        :param nums: A list of integers.
        :return: The sum of all good subsequences modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7
        maxVal = max(nums)
        limit = maxVal + 2
        counts = [0] * limit
        totalSums = [0] * limit

        for num in nums:
            currentCount = 1
            currentSum = num

            if num > 0:
                prevCount = counts[num - 1]
                prevSum = totalSums[num - 1]
                currentCount += prevCount
                currentSum += prevSum + prevCount * num

            if num + 1 < limit:
                nextCount = counts[num + 1]
                nextSum = totalSums[num + 1]
                currentCount += nextCount
                currentSum += nextSum + nextCount * num

            counts[num] = (counts[num] + currentCount) % mod
            totalSums[num] = (totalSums[num] + currentSum) % mod

        return sum(totalSums) % mod