# Leetcode 3561: Resulting String After Adjacent Removals
# https://leetcode.com/problems/resulting-string-after-adjacent-removals/
# Solved on 8th of December, 2025
class Solution:
    def resultingString(self, s: str) -> str:
        """
        Given a string s, remove adjacent characters that are "close" to each other.
        Two characters are considered "close" if the absolute difference of their ASCII values
        is 1 or 25 (to handle 'a' and 'z' wrapping around).

        Args:
            s (str): The input string.
        Returns:
            str: The resulting string after all possible adjacent removals.
        """
        charStack = []

        for currentChar in s:
            if charStack:
                topChar = charStack[-1]
                diff = abs(ord(currentChar) - ord(topChar))
                if diff == 1 or diff == 25:
                    charStack.pop()
                else:
                    charStack.append(currentChar)
            else:
                charStack.append(currentChar)

        return "".join(charStack)