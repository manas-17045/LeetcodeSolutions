# Leetcode 3084: Count Substrings Starting and Ending with Given Character
# https://leetcode.com/problems/count-substring-starting-and-ending-with-given-character/
# Solved on 6th of September, 2025
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        """
        Counts the number of substrings in 's' that contain the character 'c' at least once.
        :param s: The input string.
        :param c: The character to count occurrences of.
        :return: The total number of substrings containing 'c'.
        """
        # Count occurrences of character c in s
        k = 0
        # Assume c is a single character
        ch = c[0]
        for ch_s in s:
            if ch_s == ch:
                k += 1

        # Each single occurrence counts, and each pair of occurrences defines a substring
        return k * (k + 1) // 2