# Leetcode 2839: Check if Strings Can be Made Equal With Operations I
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/
# Solved on 29th of March, 2026
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        """
        Determines if two strings of length 4 can be made equal by swapping characters at indices i and j
        where |i - j| = 2.
        :param s1: The first string of length 4.
        :param s2: The second string of length 4.
        :return: True if the strings can be made equal, False otherwise.
        """
        evenMatch = (s1[0] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[2] and s1[2] == s2[0])
        oddMatch = (s1[1] == s2[1] and s1[3] == s2[3]) or (s1[1] == s2[3] and s1[3] == s2[1])
        return evenMatch and oddMatch