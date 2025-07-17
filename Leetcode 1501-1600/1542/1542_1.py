# Leetcode 1542: Find Longest Awesome Substring
# https://leetcode.com/problems/find-longest-awesome-substring/
# Solved on 17th of July, 2025
class Solution:
    def longestAwesome(self, s: str) -> int:
        """
        Finds the length of the longest "awesome" substring.

        An "awesome" substring is a substring where at most one digit appears an odd number of times.
        This is equivalent to saying that the bitmask representing the parity of digit counts
        is either 0 (all even) or has exactly one bit set (one digit odd).

        The solution uses a bitmask to keep track of the parity of digit counts encountered so far.
        `firstOccurrence[mask]` stores the first index `i` where the prefix `s[0...i]` results in `mask`.

        Args:
            s (str): The input string consisting of digits.
        Returns:
            int: The length of the longest awesome substring.
        """
        firstOccurrence = [len(s)] * 1024
        firstOccurrence[0] = -1
        maxLength = 0
        currentMask = 0

        for i, char in enumerate(s):
            digit = int(char)
            currentMask ^= (1 << digit)

            maxLength = max(maxLength, (i - firstOccurrence[currentMask]))

            for k in range(10):
                testMask = currentMask ^ (1 << k)
                maxLength = max(maxLength, (i - firstOccurrence[testMask]))

            if firstOccurrence[currentMask] == len(s):
                firstOccurrence[currentMask] = i

        return maxLength