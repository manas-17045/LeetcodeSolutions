# Leetcode 3770: Largest Prime from Consecutive Prime Sum
# https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/
# Solved on 25th of December, 2025
class Solution:
    def largestPrime(self, n: int) -> int:
        """
        Finds the largest prime number that can be expressed as the sum of consecutive prime numbers,
        where the sum does not exceed n.

        :param n: An integer representing the upper limit for the prime sum.
        :return: The largest prime number that is a sum of consecutive primes and less than or equal to n.
                 Returns 0 if no such prime exists.
        """
        if n < 2:
            return 0

        isPrime = [True] * (n + 1)
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n + 1, i):
                    isPrime[j] = False

        maxPrime = 0
        currentSum = 0

        for i in range(2, n + 1):
            if isPrime[i]:
                currentSum += i
                if currentSum > n:
                    break
                if isPrime[currentSum]:
                    maxPrime = currentSum

        return maxPrime