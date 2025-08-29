# Leetcode 2261: K Divisible Elements Subarrays
# https://leetcode.com/problems/k-divisible-elements-subarrays/
# Solved on 29th of August, 2025
class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        """
        Counts the number of distinct subarrays that satisfy the given conditions.

        Args:
            nums: A list of integers.
            k: The maximum number of divisible elements allowed in a subarray.
            p: The divisor.
        Returns:
            The number of distinct subarrays.
        """

        n = len(nums)
        trie = {}
        distinctCount = 0

        for i in range(n):
            currentNode = trie
            divisibleCount = 0
            for j in range(i, n):
                num = nums[j]
                if num % p == 0:
                    divisibleCount += 1

                if divisibleCount > k:
                    break

                if num not in currentNode:
                    currentNode[num] = {}
                    distinctCount += 1

                currentNode = currentNode[num]

        return distinctCount