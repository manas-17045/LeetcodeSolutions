# Leetcode 3271: Hash Divided String
# https://leetcode.com/problems/hash-divided-string/
# Solved on 23rd of June, 2025
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        """
        Calculates a string hash by processing the input string in blocks of length k.
        For each block, it sums the character values (a=0, b=1, ...) modulo 26,
        and converts the result back to a character.

        Args:
            s: The input string.
            k: The block length.
        Returns:
            The hashed string.
        """
        res = []
        base = ord('a')
        # Process each block of length k
        for i in range(0, len(s), k):
            total = 0
            # Sum hash values in this block
            for c in s[i:(i + k)]:
                total += ord(c) - base
            # Map back to a letter
            res.append(chr(base + (total % 26)))
        return ''.join(res)