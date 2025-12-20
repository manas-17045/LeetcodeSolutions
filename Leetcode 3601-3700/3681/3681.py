# Leetcode 3681: Maximum XOR of Subsequences
# https://leetcode.com/problems/maximum-xor-of-subsequences/
# Solved on 20th of December, 2025
class Solution:
    def maxXorSubsequences(self, nums: list[int]) -> int:
        """
        Calculates the maximum XOR sum of any subsequence of the given numbers.

        :param nums: A list of integers.
        :return: The maximum XOR sum achievable from any subsequence.
        """
        basis = [0] * 32
        for num in nums:
            for i in range(31, -1, -1):
                if (num >> i) & 1:
                    if basis[i] == 0:
                        basis[i] = num
                        break
                    num ^= basis[i]

        maxXor = 0
        for i in range(31, -1, -1):
            if (maxXor ^ basis[i]) > maxXor:
                maxXor ^= basis[i]

        return maxXor