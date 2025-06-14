# Leetcode 2566: Maximum Difference by Remapping a Digit
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
# Solved on 14th of June, 2025

class Solution:
    def minMaxDifference(self, num: int) -> int:
        """
        Given a 0-indexed integer num, re-arrange the digits of num at most once
        to make it the largest possible number, and re-arrange the digits of num
        at most once to make it the smallest possible number.
        Return the difference between the largest and smallest number.

        :param num: The input integer.
        :return: The difference between the largest and smallest possible numbers.
        """
        s = str(num)
        min_val = float('inf')
        max_val = float('-inf')

        # Try every possible remapping d1 -> d2
        for d1 in '0123456789':
            for d2 in '0123456789':
                # Build the new string after remapping all d1 -> d2
                t = ''.join((d2 if ch == d1 else ch) for ch in s)
                # Convert to int (this automatically drops any leading zeros)
                v = int(t)
                # Track global min/max
                if v < min_val:
                    min_val = v
                if v > max_val:
                    max_val = v

        return max_val - min_val