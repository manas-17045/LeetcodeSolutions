# Leetcode 3084: Count Substrings Starting and Ending with Given Character
# https://leetcode.com/problems/count-substring-starting-and-ending-with-given-character/
# Solved on 6th of September, 2025
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        """
        Counts the number of substrings in a given string 's' that start and end with a specific character 'c'.

        Args:
            s (str): The input string.
            c (str): The character that substrings must start and end with.
        Returns:
            int: The total number of such substrings.
        """
        charCount = s.count(c)
        totalSubstrings = charCount * (charCount + 1) // 2
        return totalSubstrings