# Leetcode 2572: Count the Number of Square-Free Subsets
# https://leetcode.com/problems/count-the-number-of-square-free-subsets/
# Solved on 29th of November, 2025
class Solution:
    def squareFreeSubsets(self, nums: list[int]) -> int:
        """
        Counts the number of square-free subsets from the given list of numbers.

        Args:
            nums: A list of integers.
        Returns:
            The number of square-free subsets modulo 10^9 + 7.
        """
        mod = 1000000007
        primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        numFreq = {}
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1

        dpArray = [0] * 1024
        dpArray[0] = 1

        for candidate in range(2, 31):
            if candidate not in numFreq:
                continue

            mask = 0
            tempVal = candidate
            isSquareFree = True

            for i in range(10):
                prime = primeList[i]
                if tempVal % (prime * prime) == 0:
                    isSquareFree = False
                    break
                if tempVal % prime == 0:
                    mask |= (1 << i)

            if not isSquareFree:
                continue

            count = numFreq[candidate]
            for state in range(1023, -1, -1):
                if (state & mask) == 0:
                    dpArray[state | mask] = (dpArray[state | mask] + dpArray[state] * count) % mod

        totalResult = sum(dpArray) % mod
        onesCount = numFreq.get(1, 0)
        totalResult = (totalResult * pow(2, onesCount, mod)) % mod
        totalResult = (totalResult - 1 + mod) % mod

        return totalResult
