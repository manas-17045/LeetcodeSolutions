# Leetcode 3918: Sum of Primes Between Number and Its Reverse
# https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/
# Solved on 19th of May, 2026
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        """
        Calculates the sum of all prime numbers between a given integer n and its reverse.

        :param n: The input integer to compare with its reverse.
        :return: The sum of prime numbers in the range [min(n, reverse(n)), max(n, reverse(n))].
        """
        reversedNumber = int(str(n)[::-1])
        rangeStart = min(n, reversedNumber)
        rangeEnd = max(n, reversedNumber)

        if rangeEnd < 2:
            return 0

        isPrime = [True] * (rangeEnd + 1)
        isPrime[0] = False
        isPrime[1] = False

        currentDivisor = 2
        while currentDivisor * currentDivisor <= rangeEnd:
            if isPrime[currentDivisor]:
                for multiple in range(currentDivisor * currentDivisor, rangeEnd + 1, currentDivisor):
                    isPrime[multiple] = False
            currentDivisor += 1

        totalPrimeSum = 0
        for currentNum in range(rangeStart, rangeEnd + 1):
            if isPrime[currentNum]:
                totalPrimeSum += currentNum

        return totalPrimeSum