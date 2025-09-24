# Leetcode 2840: Check if Strings Can be Made Equal With Operations II
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
# Solved on 24th of September, 2025
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        """
        Checks if two strings s1 and s2 can be made equal by swapping characters at even indices with other even indices,
        and characters at odd indices with other odd indices.
        :param s1: The first string.
        :param s2: The second string.
        :return: True if the strings can be made equal, False otherwise.
        """
        if len(s1) != len(s2):
            return False

        # cnt[0] for even positions, cnt[1] for odd positions
        cnt = [[0] * 26 for _ in range(2)]

        for i, (a, b) in enumerate(zip(s1, s2)):
            p = i & 1
            cnt[p][ord(a) - 97] += 1
            cnt[p][ord(b) - 97] -= 1

        # If all counts are zero for both parties, multi-sets match
        return all(x == 0 for row in cnt for x in row)