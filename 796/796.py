# Leetcode 796: Rotate String
# https://leetcode.com/problems/rotate-string/
# Solved on 3rd of May, 2026
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Checks if the string 's' can become 'goal' after some number of shifts.

        :param s: The source string to be rotated.
        :param goal: The target string to match.
        :return: True if s can be rotated to match goal, False otherwise.
        """
        if len(s) != len(goal):
            return False

        doubledString = s + s
        return goal in doubledString