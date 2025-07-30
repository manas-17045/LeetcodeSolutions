# Leetcode 2904: Shortest and Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/
# Solved on 30th of July, 2025
class Solution:
    def shortestBeautifulString(self, s: str, k: int) -> str:
        """
        Finds the shortest beautiful binary string (contains exactly k ones and no leading zeros).
        If multiple such strings exist, returns the lexicographically smallest one.
        :param s: The input binary string.
        :param k: The required number of '1's in the beautiful string.
        :return: The shortest beautiful string, or an empty string if none exists.
        """
        n = len(s)
        l = 0
        count1 = 0
        best_len = float('inf')
        best_sub = ""

        for r, ch in enumerate(s):
            # Expand right end
            if ch == '1':
                count1 += 1

            # If too many '1's, shrink from left until at most k
            while count1 > k:
                if s[l] == '1':
                    count1 -= 1
                l += 1

            # If exactly k ones, drop leading zeros and record answer
            if count1 == k:
                # Permanently drop any leading zeros to minimize length
                while l <= r and s[l] == '0':
                    l += 1
                curr_len = r - l + 1
                # substring now has exactly k ones and no leading zero
                curr_sub = s[l:r + 1]
                # Pick shorter, or same‑length but lexicographically smaller
                if curr_len < best_len or (curr_len == best_len and curr_sub < best_sub):
                    best_len = curr_len
                    best_sub = curr_sub

        return best_sub