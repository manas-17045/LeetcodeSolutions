# Leetcode 2478: Number of Beautiful Partitions
# https://leetcode.com/problems/number-of-beautiful-partitions/
# Solved on 21st of September, 2025
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        """
        Calculates the number of beautiful partitions of a string s.

        Args:
            s (str): The input string consisting of digits.
            k (int): The number of partitions required.
            minLength (int): The minimum length of each partition.

        Returns (int): The number of beautiful partitions.
        """

        n = len(s)
        mod = 10**9 + 7

        primes = {'2', '3', '5', '7'}

        def isPrime(char):
            return char in primes

        if not isPrime(s[0]) or isPrime(s[n - 1]):
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, (k + 1)):
            newDp = [0] * (n + 1)
            runningSum = 0
            for j in range(i * minLength, (n + 1)):
                p = j - minLength

                if isPrime(s[p]):
                    runningSum = (runningSum + dp[p]) % mod

                if not isPrime(s[j - 1]):
                    newDp[j] = runningSum

            dp = newDp

        return dp[n]