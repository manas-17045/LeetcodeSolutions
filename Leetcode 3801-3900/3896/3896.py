# Leetcode 3896: Minimum Operations to Transform Array into Alternating Prime
# https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/
# Solved on 19th of April, 2026
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum operations to transform the array into an alternating prime sequence.

        Args:
            nums (list[int]): A list of integers to be transformed.
        Returns:
            int: The total minimum number of operations required.
        """
        maxLimit = 100004
        isPrime = [True] * maxLimit
        isPrime[0] = False
        isPrime[1] = False

        for i in range(2, int(maxLimit ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, maxLimit, i):
                    isPrime[j] = False

        nextPrime = [0] * maxLimit
        lastPrime = 100003

        for i in range(maxLimit - 1, -1, -1):
            if isPrime[i]:
                lastPrime = i
            nextPrime[i] = lastPrime

        totalOps = 0

        for i in range(len(nums)):
            currNum = nums[i]
            if i % 2 == 0:
                totalOps += nextPrime[currNum] - currNum
            else:
                if currNum == 2:
                    totalOps += 2
                elif isPrime[currNum]:
                    totalOps += 1

        return totalOps