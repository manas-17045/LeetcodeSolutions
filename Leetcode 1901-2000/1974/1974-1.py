# Leetcode 1974: Minimum Time to Type Word Using Special Typewriter
# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
# Solved on 30th of August, 2025
class Solution:
    def minTimeToType(self, word: str) -> int:
        """
        Calculates the minimum time to type a given word using a special typewriter.

        Args:
            word (str): The word to be typed.
        Returns:
            int: The minimum time required to type the word.
        """
        totalSeconds = 0
        currentPointer = 'a'

        for char in word:
            distance = abs(ord(char) - ord(currentPointer))
            moveTime = min(distance, (26 - distance))
            totalSeconds += moveTime + 1
            currentPointer = char

        return totalSeconds