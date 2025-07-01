# Leetcode 917: Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/
# Solved on 1st of July, 2025
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Reverses only the letters in a string, leaving non-alphabetic characters in their original positions.

        Args:
            s (str): The input string.

        Returns:
            str: The string with only letters reversed.
        """
        # Convert to list, so we can swap in-place
        chars = list(s)
        i, j = 0, (len(chars) - 1)

        while i < j:
            # Move i forward until it points at a letter
            if not chars[i].isalpha():
                i += 1
                continue
            # Move j backward until it points at a letter
            if not chars[j].isalpha():
                j -= 1
                continue

            # Both chars[i] and chars[j] are letters-swap them
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1

        # Reconstruct string
        return ''.join(chars)