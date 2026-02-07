# Leetcode 1653: Minimum Deletions to Make String Balanced
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
# Solved on 7th of February, 2026
class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        Calculates the minimum number of deletions needed to make the string balanced.

        :param s: A string consisting only of characters 'a' and 'b'.
        :return: The minimum number of deletions required.
        """
        bCount = 0
        minDeletions = 0

        for char in s:
            if char == 'b':
                bCount += 1
            else:
                minDeletions = min(minDeletions + 1, bCount)

        return minDeletions