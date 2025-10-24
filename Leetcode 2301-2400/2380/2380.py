# Leetcode 2380: Time Needed to Rearrange a Binary String
# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/
# Solved on 24th of October, 2025
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        """
        Calculates the minimum time needed to rearrange a binary string such that all '0's are to the left
        and all '1's are to the right.

        Args:
            s: The binary string.
        Returns:
            The minimum number of seconds required for the rearrangement.
        """
        seconds = 0
        zeros = 0
        for c in s:
            if c == '0':
                zeros += 1
            elif zeros > 0:
                seconds = max(seconds + 1, zeros)

        return seconds