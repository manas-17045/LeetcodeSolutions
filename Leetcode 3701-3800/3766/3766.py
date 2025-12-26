# Leetcode 3766: Minimum Operations to Make Binary Palindrome
# https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/
# Solved on 26th of December, 2025
from bisect import bisect_left


class Solution:
    def minOperations(self, nums: list[int]) -> list[int]:
        """
        Calculates the minimum operations to make each number in `nums` a binary palindrome.

        :param nums: A list of integers.
        :return: A list of integers, where each element is the minimum operations required for the corresponding number in `nums`.
        """
        palindromes = []
        for length in range(1, 14):
            halfLength = (length + 1) // 2
            start = 1 << (halfLength - 1)
            end = 1 << halfLength
            for i in range(start, end):
                binaryPrefix = bin(i)[2:]
                if length % 2 == 1:
                    palindromeStr = binaryPrefix + binaryPrefix[:-1][::-1]
                else:
                    palindromeStr = binaryPrefix + binaryPrefix[::-1]
                palindromes.append(int(palindromeStr, 2))

        palindromes.sort()

        result = []
        for num in nums:
            index = bisect_left(palindromes, num)
            minOps = float('inf')

            if index < len(palindromes):
                minOps = min(minOps, palindromes[index] - num)

            if index > 0:
                minOps = min(minOps, num - palindromes[index - 1])

            result.append(minOps)

        return result