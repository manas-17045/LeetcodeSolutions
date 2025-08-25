# Leetcode 2075: Decode the Slanted Ciphertext
# https://leetcode.com/problems/decode-the-slanted-ciphertext/
# Solved on 25th of August, 2025
class Solution:
    def decodeCipherText(self, encodedText: str, rows: int) -> str:
        """
        Decodes a cipher text that was encoded using a diagonal traversal method.
        Args:
            encodedText (str): The encoded string.
            rows (int): The number of rows used during encoding.
        Returns:
            str: The decoded original string.
        """
        n = len(encodedText)
        if rows <= 0 or n == 0:
            return ""
        cols = n // rows

        res_chars = []
        # Start a diagonal from each column in the first row
        for start_col in range(cols):
            r = 0
            c = start_col
            # Advance down-right along the diagonal
            while r < rows and c < cols:
                idx = r * cols + c
                res_chars.append(encodedText[idx])
                r += 1
                c += 1

        # Remove trailing spaces introduced by padding (but keep internal spaces)
        return "".join(res_chars).rstrip()