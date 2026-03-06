# Leetcode 1784: Check if Binary String Has at Most One Segment of Ones
# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
# Solved on 6th of March, 2026
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """
        Checks if the binary string s contains at most one contiguous segment of ones.

        :param s: A binary string consisting of '0's and '1's.
        :return: True if there is at most one segment of ones, False otherwise.
        """
        hasMultipleSegments = "01" in s
        return not hasMultipleSegments