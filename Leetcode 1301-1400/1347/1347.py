# Leetcode 1347: Minimum Number of Steps to Make Two Strings Anagram
# https://leetcode.com/problems/minimum-number-of0steps-to-make-two-strings-anagram/
# Solved on 4th of December, 2025
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        Calculates the minimum number of steps required to make two strings anagrams.
        A step consists of changing one character in string t to another character.

        Args:
            s (str): The first string.
            t (str): The second string.
        Returns:
            int: The minimum number of steps.
        """
        charCount = [0] * 26
        for char in s:
            charCount[ord(char) - ord('a')] += 1
        for char in t:
            charCount[ord(char) - ord('a')] -= 1

        steps = 0
        for count in charCount:
            if count > 0:
                steps += count

        return steps