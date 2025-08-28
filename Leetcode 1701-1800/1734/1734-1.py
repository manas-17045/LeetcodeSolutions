# Leetcode 1734: Decode XORed Permutation
# https://leetcode.com/problems/decode-xored-permutation/
# Solved on 28th of August, 2025
class Solution:
    def decode(self, encoded: list[int]) -> list[int]:
        """
        Decodes a XORed permutation.

        Args:
            encoded (list[int]): The encoded array where encoded[i] = perm[i] ^ perm[i + 1].

        Returns:
            list[int]: The original permutation array.
        """
        n = len(encoded) + 1

        totalXor = 0
        for i in range(1, n + 1):
            totalXor ^= i

        oldIndicesXor = 0
        for i in range(1, len(encoded), 2):
            oldIndicesXor ^= encoded[i]

        firstElement = totalXor ^ oldIndicesXor

        perm = [0] * n
        perm[0] = firstElement

        for i in range(n - 1):
            perm[i + 1] = perm[i] ^ encoded[i]

        return perm