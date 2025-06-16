# Leetcode 3514: Number of Unique XOR Triplets II
# https://leetcode.com/problems/number-of-unique-xor-triplets-ii/
# Solved on 16th of June, 2025

class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        """
        Calculates the number of unique XOR triplets (a, b, c) where a, b, and c are elements
        from the input list `nums`, and a ^ b ^ c is a unique value.

        Args:
            nums: A list of integers.

        Returns:
            The number of unique XOR values that can be formed by XORing three elements from `nums`.
        """
        n = len(nums)
        uniqueXorValues = set()

        pairwiseXorsOfSuffix = set()

        for i in range((n - 1), -1, -1):
            for xorPair in pairwiseXorsOfSuffix:
                uniqueXorValues.add(nums[i] ^ xorPair)

            for k in range(i, n):
                uniqueXorValues.add(nums[k])
                pairwiseXorsOfSuffix.add(nums[i] ^ nums[k])

        return len(uniqueXorValues)