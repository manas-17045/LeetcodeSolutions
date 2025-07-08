# Leetcode 1520: Maximum Number of Non-Overlapping Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
# Solved on 8th of July, 2025
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        """
        Finds the maximum number of non-overlapping substrings such that each substring contains
        all occurrences of its constituent characters.

        A substring `t` is valid if for every character `c` in `t`, all occurrences of `c` in `s`
        are also within `t`.

        The goal is to find the maximum number of such valid substrings that are non-overlapping.

        Args:
            s: The input string.
        Returns:
            A list of the valid non-overlapping substrings.
        """
        n = len(s)
        # Record each character's first and last occurrence.
        first = [n] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = max(last[idx], i)

        intervals = []
        # For each character, try to build the minimal covering interval.
        for c in range(26):
            if last[c] == -1:
                # Character doesn't appear
                continue
            l, r = first[c], last[c]
            j = l
            valid = True
            # Expand window to include all occurrences of any char inside [l...r]
            while j <= r:
                cj = ord(s[j]) - ord('a')
                # If this character's first occurrence is before our start,
                # then this interval would overlap with some earlier interval
                if first[cj] < l:
                    valid = False
                    break
                # Expand to cover all of cj
                r = max(r, last[cj])
                j += 1

            if valid:
                intervals.append((l, r))

        # Greedily select the maximum number of non-overlapping intervals
        intervals.sort(key=lambda x: x[1])
        ans = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                ans.append(s[l:(r+ 1)])
                prev_end = r

        return ans