# Leetcode 1540: Can Convert String in K Moves
# https://leetcode.com/problems/can-convert-string-in-k-moves/
# Solved on 24th of September, 2025
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        """
        Determines if string `s` can be converted to string `t` within `k` moves.
        :param s: The source string.
        :param t: The target string.
        :param k: The maximum number of moves allowed.
        :return: True if `s` can be converted to `t` within `k` moves, False otherwise.
        """
        if len(s) != len(t):
            return False

        shiftCounts = [0] * 26

        for i in range(len(s)):
            if s[i] == t[i]:
                continue

            diff = (ord(t[i]) - ord(s[i]) + 26) % 26

            requiredMove = diff + shiftCounts[diff] * 26

            if requiredMove > k:
                return False

            shiftCounts[diff] += 1

        return True