# Leetcode 3614: Process String with Special Operations II
# https://leetcode.com/problems/process-string-with-special-operations-ii/
# Solved on 19th of December, 2025
class Solution:
    def processStr(self, s: str, k: int) -> str:
        """
        Processes a string with special operations and returns the character at a specific index k.

        Args:
            s: The input string containing characters and special operation symbols.
            k: The 0-indexed position to find the character.
        Returns:
            The character at index k after processing, or '.' if k is out of bounds.
        """
        n = len(s)
        lengths = [0] * n
        currentLength = 0

        for i, char in enumerate(s):
            if char == '*':
                currentLength = max(0, currentLength - 1)
            elif char == '#':
                currentLength *= 2
            elif char == '%':
                pass
            else:
                currentLength += 1
            lengths[i] = currentLength

        if k >= lengths[n - 1]:
            return "."

        for i in range(n - 1, -1, -1):
            char = s[i]
            currentLength = lengths[i]
            prevLength = lengths[i - 1] if i > 0 else 0

            if char.islower():
                if k == prevLength:
                    return char
            elif char == '#':
                if k >= prevLength:
                    k -= prevLength
            elif char == '%':
                k = currentLength - 1 - k

        return "."