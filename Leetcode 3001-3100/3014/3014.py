# Leetcode 3014: Minimum Number of Pushes to Type Word I
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/
# Solved on 30th of July, 2026
class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Calculates the minimum number of pushes required to type a given word on a phone keypad.
        
        The method assigns the first 8 letters to the 1st position (1 push each),
        the next 8 letters to the 2nd position (2 pushes each), and so on.
        
        @param word The input string to be typed.
        @return The minimum total number of pushes required.
        """
        wordLength = len(word)
        fullGroups = wordLength // 8
        remainingLetters = wordLength % 8

        return (4 * fullGroups + remainingLetters) + (fullGroups + 1)