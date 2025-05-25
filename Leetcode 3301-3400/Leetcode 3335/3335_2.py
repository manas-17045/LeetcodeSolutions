# Leetcode 3335: Total Characters in String After Transformations I
# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
# Solved on 13th of May, 2025

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        """
        Calculates the total length of the string after applying a series of transformations.

        Args:
            s: The input string consisting of lowercase English letters.
            t: The number of transformations to apply.

        Returns:
            The total length of the transformed string modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # char_lengths[i] will store the length of the string
        # derived from character (ord('a') + i) after k transformations.
        # Initialize for 0 transformations: length is 1 for any single char.
        char_lengths = [1] * 26

        for k in range(1, t + 1):
            next_char_lengths = [0] * 26
            # For 'a' through 'y' (char_code 0 through 24)
            for char_code in range(25): # 0 to 24
                # char_code transforms to char_code + 1
                next_char_lengths[char_code] = char_lengths[char_code + 1]

            # For 'z' (char_code 25)
            # 'z' transforms to "ab"
            # contributions from 'a' (char_code 0) and 'b' (char_code 1)
            next_char_lengths[25] = (char_lengths[0] + char_lengths[1]) % MOD

            char_lengths = next_char_lengths

        # Calculate total length for the input string s
        total_final_length = 0
        for original_char_in_s in s:
            code = ord(original_char_in_s) - ord('a')
            total_final_length = (total_final_length + char_lengths[code]) % MOD

        return total_final_length