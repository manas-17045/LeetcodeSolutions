# Leetcode 2048: Next Greater Numerically Balanced Number
# https://leetcode.com/problems/next-greater-numerically-balanced-number/
# Solved on 24th of October, 2025
import bisect
from itertools import permutations


class Solution:
    combinationsList = [
        "1",
        "22",
        "122", "333",
        "1333", "4444",
        "14444", "22333", "55555",
        "122333", "155555", "224444", "666666"
    ]

    balancedNums = set()
    for s in combinationsList:
        for p in set(permutations(s)):
            balancedNums.add(int("".join(p)))

    balancedNums.add(1224444)

    sortedBalancedNums = sorted(list(balancedNums))

    def nextBeautifulNumber(self, n: int) -> int:
        """
        Finds the smallest numerically balanced number strictly greater than n.

        :param n: The input integer.
        :return: The smallest numerically balanced number strictly greater than n.
        """
        index = bisect.bisect_right(self.sortedBalancedNums, n)
        return self.sortedBalancedNums[index]