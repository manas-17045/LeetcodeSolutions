# Leetcode 2075: Decode the Slanted Ciphertext
# https://leetcode.com/problems/decode-the-slanted-ciphertext/
# Solved on 25th of August, 2025
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        """
        Decodes a slanted ciphertext.

        Args:
            encodedText (str): The encoded string.
            rows (int): The number of rows used for encoding.
        Returns:
            str: The decoded string.
        """
        textLength = len(encodedText)
        if textLength == 0:
            return ""

        cols = textLength // rows
        decodedChars = []

        for startCol in range(cols):
            row = 0
            col = startCol
            while row < rows and col < cols:
                index = row * cols + col
                decodedChars.append(encodedText[index])
                row += 1
                col += 1

        return "".join(decodedChars).rstrip()