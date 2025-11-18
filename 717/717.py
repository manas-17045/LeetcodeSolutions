# Leetcode 717: 1-bit and 2-bit Characters
# https://leetcode.com/problems/1-bit-and-2-bit-characters/
# Solved on 18th of November, 2025
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        """
        Determines if the last character in a given array of bits can be represented as a one-bit character.

        Args:
            bits: A list of integers, where each integer is either 0 or 1.

        Returns:
            True if the last character can be represented as a one-bit character, False otherwise.
        """
        currentIndex = 0
        arrayLength = len(bits)
        while currentIndex < arrayLength - 1:
            if bits[currentIndex] == 1:
                currentIndex += 2
            else:
                currentIndex += 1

        return currentIndex == arrayLength - 1