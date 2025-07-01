# Leetcode 2810: Faulty Keyboard
# https://leetcode.com/problems/faulty-keyboard/
# Solved on 1st of July, 2025
class Solution:
    def finalString(self, s: str) -> str:
        """
        Given a 0-indexed string s, reverse the result string each time you encounter the character 'i'.
        Any other character is appended to the result string.

        Args:
            s (str): The input string.
        Returns:
            str: The final string after processing all characters.
        """
        stringBuilder = []

        for character in s:
            if character == 'i':
                stringBuilder.reverse()
            else:
                stringBuilder.append(character)

        return "".join(stringBuilder)