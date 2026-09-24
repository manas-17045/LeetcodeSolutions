# Leetcode 4032: Longest Subarrays With at Most K Distinct Prime Factors
# https://leetcode.com/problems/longest-subarrays-with-at-most-k-distinct-prime-factors/
# Solved on 24th of September, 2026
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        """
        Finds the length of the longest subarray containing at most k distinct prime factors.

        Parameters:
            nums (list[int]): An array of positive integers.
            k (int): The maximum number of distinct prime factors allowed.

        Returns:
            int: The length of the longest valid subarray, or 0 if none exists.
        """
        maxNumber = max(nums)
        smallestPrime = list(range(maxNumber + 1))
        sieveLimit = int(maxNumber ** 0.5) + 1

        for factor in range(2, sieveLimit):
            if smallestPrime[factor] == factor:
                for multiple in range(factor * factor, maxNumber + 1, factor):
                    if smallestPrime[multiple] == multiple:
                        smallestPrime[multiple] = factor

        factorMap = {}
        for number in set(nums):
            factors = []
            tempNumber = number
            while tempNumber > 1:
                prime = smallestPrime[tempNumber]
                factors.append(prime)
                while tempNumber % prime == 0:
                    tempNumber //= prime
            factorMap[number] = factors

        primeFrequencies = [0] * (maxNumber + 1)
        distinctPrimes = 0
        leftPointer = 0
        maxLength = 0

        for rightPointer in range(len(nums)):
            for prime in factorMap[nums[rightPointer]]:
                if primeFrequencies[prime] == 0:
                    distinctPrimes += 1
                primeFrequencies[prime] += 1

            while distinctPrimes > k:
                for prime in factorMap[nums[leftPointer]]:
                    primeFrequencies[prime] -= 1
                    if primeFrequencies[prime] == 0:
                        distinctPrimes -= 1
                leftPointer += 1
            
            currentLength = rightPointer -leftPointer + 1
            if currentLength > maxLength:
                maxLength = currentLength

        return maxLength