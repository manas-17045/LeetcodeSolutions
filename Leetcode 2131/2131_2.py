# Leetcode 2131: Longest palindrome by Concatenating Two Letter Words
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
# Solved on 25th of May, 2025
from collections import Counter


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        """
        Finds the length of the longest palindrome that can be built by concatenating
        two-letter words from the given list.

        Args:
            words: A list of two-letter strings.

        Returns:
            The length of the longest palindrome that can be formed.

        """

        cnt = Counter(words)
        ans = 0
        center_used = False

        for w, c in cnt.items():
            rev = w[::-1]
            if w == rev:
                # words like "gg", "aa"
                # we can pair up floor(c/2) of them on both sides
                pairs = c // 2
                ans += pairs * 4
                # If there's an odd one left, we can potentially put exactly one in the center
                if c % 2 == 1:
                    center_used = True
            else:
                # For non-palindrome words, match with their reverse
                # to avoid double counting, only handle one ordering
                if w < rev:
                    ans += min(c, cnt.get(rev, 0)) * 4

        # If we had atleast one odd-count palindrome, put one in the middle
        if center_used:
            ans += 2

        return ans