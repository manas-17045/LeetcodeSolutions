# Leetcode 1585: Check If String Is Transformable With Substring Sort Operations
# https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/
# Solved on 12th of September, 2025
from collections import deque


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        """
        Determines if string s can be transformed into string t by moving digits.

        Args:
            s (str): The source string consisting of digits.
            t (str): The target string consisting of digits.
        Returns:
            bool: True if s can be transformed into t, False otherwise.
        """
        # positions[d] will store indices of digit d in s (in increasing order)
        positions = [deque() for _ in range(10)]
        for i, ch in enumerate(s):
            positions[int(ch)].append(i)

        # For each digit in t, pick the earliest occurrence in s and ensure
        # no smaller digit has an occurrence to its left (which would block movement).
        for ch in t:
            d = int(ch)
            if not positions[d]:
                return False

            idx = positions[d].popleft()
            # If any smaller digit has its earliest remaining index < idx, we cannot move d past it
            for smaller in range(d):
                if positions[smaller] and positions[smaller][0] < idx:
                    return False

        return True