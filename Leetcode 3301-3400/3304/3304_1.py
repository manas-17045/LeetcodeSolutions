# Leetcode 3304: Find the K-th Character in String Game I
# https://leetcode.com/problems/find-the-k-th-character-in-the-string-game-i/
# Solved on 3rd of July, 2025
class Solution:
    def kthCharacter(self, k: int) -> str:
        """
        Finds the k-th character in the string game.

        The k-th character is determined by the parity of the popcount (number of set bits)
        of (k-1). The offset from 'a' is (popcount % 26).
        """
        kMinusOne = k - 1
        popCount = bin(kMinusOne).count('1')
        offset = popCount % 26
        finalChar = chr(ord('a') + offset)
        return finalChar