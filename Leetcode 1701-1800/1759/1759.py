# Leetcode 1759: Count Number of Homogeneous Substrings
# https://leetcode.com/problems/count-number-of-homogenous-substrings/
# Solved on 16th of November, 2025
class Solution:
    def countHomogenous(self, s: str) -> int:
        """
        Counts the total number of homogeneous substrings in a given string.
        A homogeneous substring is a substring where all characters are the same.

        Args:
            s (str): The input string.
        Returns:
            int: The total count of homogeneous substrings, modulo 10^9 + 7.
        """
        modValue = 1000000007
        totalCount = 0
        currentStreak = 0

        for i in range(len(s)):
            if i == 0 or s[i] != s[i - 1]:
                currentStreak = 1
            else:
                currentStreak += 1

            totalCount = (totalCount + currentStreak) % modValue

        return totalCount