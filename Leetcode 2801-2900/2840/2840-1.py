# Leetcode 2840: Check if Strings Can be Made Equal With Operations II
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
# Solved on 24th of September, 2025
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        Checks if two strings s1 and s2 can be made equal with operations.
        An operation consists of swapping any two characters at even indices or any two characters at odd indices.

        Args:
            s1 (str): The first string.
            s2 (str): The second string.
        Returns:
            bool: True if s1 and s2 can be made equal, False otherwise.
        """
        s1EvenCounts = [0] * 26
        s1OddCounts = [0] * 26
        s2EvenCounts = [0] * 26
        s2OddCounts = [0] * 26

        stringLength = len(s1)

        for i in range(stringLength):
            if i % 2 == 0:
                s1EvenCounts[ord(s1[i]) - ord('a')] += 1
                s2EvenCounts[ord(s2[i]) - ord('a')] += 1
            else:
                s1OddCounts[ord(s1[i]) - ord('a')] += 1
                s2OddCounts[ord(s2[i]) - ord('a')] += 1

        return s1EvenCounts == s2EvenCounts and s1OddCounts == s2OddCounts