# Leetcode 4043: Count Rotations With Exactly K Equal Adjacent Pairs
# https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/
# Solved on 4th of October, 2026
class Solution:
    def countRotations(self, s: str, k: int) -> int:
        """
        Counts the number of cyclic rotations of a string that have exactly k equal adjacent character pairs.

        Args:
            s (str): The input string of lowercase English letters.
            k (int): The target score representing equal adjacent pairs.

        Returns:
            int: The number of cyclic rotations whose score equals k.
        """
        stringLength = len(s)
        circularMatches = 0

        for charIndex in range(stringLength):
            if s[charIndex] == s[(charIndex + 1) % stringLength]:
                circularMatches += 1

        totalCount = 0

        if k == circularMatches - 1:
            totalCount += circularMatches

        if k == circularMatches:
            totalCount += stringLength - circularMatches

        return totalCount