# Leetcode 1734: Decode XORed Permutation
# https://leetcode.com/problems/decode-xored-permutation/
# Solved on 28th of August, 2025
class Solution:
    def decode(self, encoded: list[int]) -> list[int]:
        """
        Decodes a given `encoded` array to reconstruct the original `perm` array.

        Args:
            encoded (list[int]): An array where encoded[i] = perm[i] ^ perm[i+1].
        Returns:
            list[int]: The original permutation array `perm`.
        """
        n = len(encoded) + 1

        # XOR of numbers 1..n
        total_xor = 0
        for num in range(1, n + 1):
            total_xor ^= num

        # XOR of encoded elements at odd indices: encoded[1], encoded[3], ...
        # This equals perm[1] ^ perm[2] ^ ... ^ perm[n-1] (all except perm[0])
        odd_xor = 0
        for i in range(1, len(encoded), 2):
            odd_xor ^= encoded[i]

        # perm[0] = total_xor ^ odd_xor
        perm0 = total_xor ^ odd_xor

        perm = [0] * n
        perm[0] = perm0
        for i in range(len(encoded)):
            perm[i + 1] = perm[i] ^ encoded[i]

        return perm