# Leetcode 2781: Length of the Longest Valid Substring
# https://leetcode.com/problems/length-of-the-longest-valid-substring/
# Solved on 19th of July, 2025
class Solution:
    def longestValidSubstring(self, word: str, forbidden: list[str]) -> int:
        """
        Finds the length of the longest valid substring of 'word' that does not contain any substring from 'forbidden'.
        :param word: The input string.
        :param forbidden: A list of forbidden substrings.
        :return: The length of the longest valid substring.
        """
        # Preprocess forbidden list into a set for O(1) lookups
        forbidden_set = set(forbidden)
        # Maximum length of any forbidden substring
        max_forbid_len = max((len(s) for s in forbidden), default=0)
        n = len(word)
        # Left boundary of the current valid window (inclusive)
        left = 0
        ans = 0
        # Iterate through the string with right pointer
        for i in range(n):
            # Check substrings ending at i of length up to max_forbid_len
            # If any forbidden substring is found, move left just after its start
            for l in range(1, min(max_forbid_len, i - left + 1) + 1):
                start = i - l + 1
                # Extract substring
                if word[start:i + 1] in forbidden_set:
                    # Move left boundary to exclude this forbidden substring
                    left = start + 1
                    # Once adjusted, no need to check shorter substrings ending at i
                    break
            # Update answer
            ans = max(ans, i - left + 1)
        return ans