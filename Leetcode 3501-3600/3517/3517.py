# Leetcode 3517: Smallest Palindromic Rearrangement I
# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/
# Solved on 31st of December, 2025
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        """
        Given a string s, rearrange its characters to form the lexicographically smallest palindrome.

        Args:
            s (str): The input string consisting of lowercase English letters.
        Returns:
            str: The lexicographically smallest palindromic rearrangement of s.
        """
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1

        halfBuilder = []
        middleChar = ""

        for i in range(26):
            currentChar = chr(ord('a') + i)
            count = frequency[i]
            halfBuilder.append(currentChar * (count // 2))

            if count % 2 == 1:
                middleChar = currentChar

        halfString = "".join(halfBuilder)
        return halfString + middleChar + halfString[::-1]