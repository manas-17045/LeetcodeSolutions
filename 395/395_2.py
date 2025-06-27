# Leetcode 395: Longest Substring with At Least K Repeating Characters
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# Solved on 27th of June, 2025
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring of s such that the frequency
        of each character in that substring is at least k.

        This solution uses a sliding window approach, iterating through all
        possible numbers of unique characters (1 to 26) that a valid substring
        could contain. For each `curr_unique` target, it maintains a window
        and expands/shrinks it to satisfy the conditions.
        """
        if k <= 1:
            return len(s)

        res = 0
        n = len(s)

        # Try every possible target for "number of unique chars" in the window
        for curr_unique in range(1, 27):
            count = [0] * 26
            start = 0
            end = 0
            unique = 0
            count_at_least_k = 0

            while end < n:
                # Expand right until we exceed the allowed number of uniques
                if unique <= curr_unique:
                    idx = ord(s[end]) - ord('a')
                    if count[idx] == 0:
                        unique += 1
                    count[idx] += 1
                    if count[idx] == k:
                        count_at_least_k += 1
                    end += 1
                else:
                    # Shrink from left to reduce unique count
                    idx = ord(s[start]) - ord('a')
                    if count[idx] == k:
                        count_at_least_k -= 1
                    count[idx] -= 1
                    if count[idx] == 0:
                        unique -= 1
                    start += 1

                # Check if current window is `perfect`:
                # 1. has exactly curr_unique distinct chars
                # 2. all of them appear at least k times
                if unique == curr_unique and unique == count_at_least_k:
                    res = max(res, end - start)

        return res