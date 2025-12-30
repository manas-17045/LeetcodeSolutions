# Leetcode 3618: Split Array by Prime Indices
# https://leetcode.com/problems/split-array-by-prime-indices/
# Solved on 30th of December, 2025
class Solution:
    def splitArray(self, nums: list[int]) -> int:
        """
        Splits the array into two parts based on prime indices and returns the absolute difference of their sums.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The absolute difference between the sum of elements at prime indices and the sum of elements at non-prime indices.
        """
        arrayLength = len(nums)
        isPrime = [True] * arrayLength
        if arrayLength > 0:
            isPrime[0] = False
        if arrayLength > 1:
            isPrime[1] = False

        for i in range(2, int(arrayLength ** 0.5) + 1):
            if isPrime[i]:
                sliceLength = len(range(i * i, arrayLength, i))
                isPrime[i * i:arrayLength:i] = [False] * sliceLength

        primeSum = 0
        totalSum = 0

        for i in range(arrayLength):
            currentValue = nums[i]
            totalSum += currentValue
            if isPrime[i]:
                primeSum += currentValue

        nonPrimeSum = totalSum - primeSum
        return abs(primeSum - nonPrimeSum)