# Leetcode 2434: Using a Robot to Print the Lexicographically Smallest String
# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
# Solved on 6th of June, 2025

class Solution:
    def robotWithString(self, s: str) -> str:
        """
        Given a string s, a robot can perform two operations:
        1. Take the leftmost character of s and append it to a paper.
        2. Take the rightmost character of the paper and append it to the result string.
        The goal is to obtain the lexicographically smallest string possible.

        Args:
            s: The input string.
        Returns:
            The lexicographically smallest string that can be obtained.
        """
        n = len(s)
        p = []
        t = []

        minSuf = [''] * (n + 1)
        minSuf[n] = '{'

        for i in range(n - 1, -1, -1):
            minSuf[i] = min(s[i], minSuf[i + 1])

        for i in range(n):
            t.append(s[i])
            while t and t[-1] <= minSuf[i + 1]:
                p.append(t.pop())

        return "".join(p)