# Leetcode 1994: The Number of Good Subsets
# https://leetcode.com/problems/the-number-of-good-subsets/
# Solved on 10th of August, 2025
import collections


class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mod = 10 ** 9 + 7

        numToMask = {}
        for i in range(2, 31):
            hasSquareFactor = False
            for p in primes:
                if i % (p * p) == 0:
                    hasSquareFactor = True
                    break

            if hasSquareFactor:
                continue

            mask = 0
            for j, p in enumerate(primes):
                if i % p == 0:
                    mask |= (1 << j)
            numToMask[i] = mask

        counts = collections.Counter(nums)

        dp = [0] * (1 << 10)
        dp[0] = 1

        for num in numToMask:
            if num in counts:
                count = counts[num]
                currentMask = numToMask[num]

                for prevMask in range((1 << 10) - 1, -1, -1):
                    if (prevMask & currentMask) == 0:
                        newMask = prevMask | currentMask
                        dp[newMask] = (dp[newMask] + dp[prevMask] * count) % mod

        totalGoodSubsets = sum(dp[1:]) % mod

        countOfOnes = counts.get(1, 0)
        if countOfOnes > 0:
            powerOfTwo = pow(2, countOfOnes, mod)
            totalGoodSubsets = (totalGoodSubsets * powerOfTwo) % mod

        return totalGoodSubsets