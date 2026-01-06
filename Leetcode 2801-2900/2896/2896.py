# Leetcode 2896: Apply Operations to Make Two Strings Equal
# https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/
# Solved on 6th of January, 2026
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        """
        Calculates the minimum operations to make two strings equal.
        :param s1: The first string.
        :param s2: The second string.
        :param x: The cost of an operation to flip two characters at different indices.
        :return: The minimum number of operations, or -1 if it's impossible.
        """
        diff = [i for i, (c1, c2) in enumerate(zip(s1, s2)) if c1 != c2]
        n = len(diff)

        if n % 2 != 0:
            return -1
        if n == 0:
            return 0

        dp0 = 0
        dp1 = x

        for i in range(1, n):
            cost = 0 if i % 2 == 1 else x
            current = min(dp1 + cost, dp0 + diff[i] - diff[i - 1])
            dp0 = dp1
            dp1 = current

        return dp1