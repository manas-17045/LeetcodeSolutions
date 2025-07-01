# Leetcode 2810: Faulty Keyboard
# https://leetcode.com/problems/faulty-keyboard/
# Solved on 1st of July, 2025
class Solution:
    def finalString(self, s: str) -> str:
        """
        Calculates the final string after processing a series of operations.

        The operations are:
        - If a character is 'i', the current string is reversed.
        - Otherwise, the character is appended to the current string.

        :param s: The input string containing characters and 'i' operations.
        :return: The final string after all operations are applied.
        """
        # Use a list as a StringBuilder
        result = []
        for ch in s:
            if ch == 'i':
                # On 'i', reverse what we have so far
                result.reverse()
            else:
                # Otherwise, append the character
                result.append(ch)
        # Join the list into the final string
        return ''.join(result)