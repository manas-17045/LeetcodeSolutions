# Leetcode 1717: Maximum Score From Removing Substrings
# https://leetcode.com/problems/maximum-score-from-removing-substrings/
# Solved on 23rd of July, 2025
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Calculates the maximum score obtainable by removing "ab" or "ba" substrings.

        Args:
            s (str): The input string.
            x (int): The points gained for removing "ab".
            y (int): The points gained for removing "ba".
        Returns:
            int: The maximum total score.
        """
        def processString(text, pair, points):
            stack = []
            gain = 0
            firstChar = pair[0]
            secondChar = pair[1]
            for char in text:
                if stack and stack[-1] == firstChar and char == secondChar:
                    stack.pop()
                    gain += points
                else:
                    stack.append(char)
            return "".join(stack), gain

        totalGain = 0
        if x > y:
            highPair = "ab"
            highPoints = x
            lowPair = "ba"
            lowPoints = y
        else:
            highPair = "ba"
            highPoints = y
            lowPair = "ab"
            lowPoints = x

        remainingString, firstGain = processString(s, highPair, highPoints)
        totalGain += firstGain

        finalString, secondGain = processString(remainingString, lowPair, lowPoints)
        totalGain += secondGain

        return totalGain