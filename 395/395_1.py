# Leetcode 395: Longest Substring with At Least K Repeating Characters
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# Solved on 27th of June, 2025
import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring of 's' such that
        every character in that substring appears at least 'k' times.

        Args:
            s (str): The input string.
            k (int): The minimum frequency required for each character
                     in the valid substring.

        Returns:
            int: The length of the longest valid substring.
        """
        if len(s) < k:
            return 0

        charCounts = collections.Counter(s)

        for aChar in charCounts:
            if charCounts[aChar] < k:
                subStrings = s.split(aChar)
                return max(self.longestSubstring(subString, k) for subString in subStrings)

        return len(s)