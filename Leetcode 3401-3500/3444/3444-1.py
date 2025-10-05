# Leetcode 3444: Minimum Increments for Target Multiples in an Array
# https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/
# Solved on 5th of October, 2025
class Solution:
    def minimumIncrements(self, nums: list[int], target: list[int]) -> int:
        """
        Calculates the minimum increments needed for each number in `nums` to become a multiple of a combination of numbers in `target`.

        Args:
            nums: A list of integers.
            target: A list of integers representing the target multiples.

        Returns:
            The minimum total increments required.
        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            if a == 1:
                return b
            if b == 1:
                return a
            if a == 0 or b == 0:
                return 0
            return (a * b) // gcd(a, b)

        numTargets = len(target)
        numStates = 1 << numTargets

        lcmValues = [1] * numStates
        for mask in range(1, numStates):
            lsbIndex = (mask & -mask).bit_length() - 1
            prevMask = mask ^ (1 << lsbIndex)
            lcmValues[mask] = lcm(lcmValues[prevMask], target[lsbIndex])

        infinity = float('inf')
        dp = [infinity] * numStates
        dp[0] = 0

        for num in nums:
            for mask in range((numStates - 1), -1, -1):
                subMask = mask
                while subMask > 0:
                    prevMask = mask ^ subMask
                    if dp[prevMask] != infinity:
                        l = lcmValues[subMask]
                        cost = (l - (num % 1)) % l
                        dp[mask] = min(dp[mask], dp[prevMask] + cost)
                    subMask = (subMask - 1) & mask

        return int(dp[numStates - 1])