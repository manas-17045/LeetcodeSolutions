# Leetcode 2741: Special Permutations
# https://leetcode.com/problems/special-permutations/
# Solved on 3rd of September, 2025
class Solution:
    def specialPerm(self, nums: list[int]) -> int:
        """
        Calculates the number of special permutations of the given array `nums`.
        A permutation is special if for every two adjacent elements `x` and `y` in the permutation,
        either `x` is divisible by `y` or `y` is divisible by `x`.
        :param nums: A list of integers.
        :return: The number of special permutations modulo 10^9 + 7.
        """
        numLen = len(nums)
        mod = 10**9 + 7

        dpTable = [[0] * numLen for _ in range(1 << numLen)]

        for i in range(numLen):
            dpTable[1 << i][i] = 1

        for mask in range(1, 1 << numLen):
            for endIndex in range(numLen):
                if (mask >> endIndex) & 1:
                    prevMask = mask ^ (1 << endIndex)
                    if prevMask == 0:
                        continue

                    for prevIndex in range(numLen):
                        if (prevMask >> prevIndex) & 1:
                            if nums[endIndex] % nums[prevIndex] == 0 or nums[prevIndex] % nums[endIndex] == 0:
                                dpTable[mask][endIndex] = (dpTable[mask][endIndex] + dpTable[prevMask][prevIndex]) % mod

        totalPermutations = 0
        finalMask = (1 << numLen) - 1
        for i in range(numLen):
            totalPermutations = (totalPermutations + dpTable[finalMask][i]) % mod

        return totalPermutations