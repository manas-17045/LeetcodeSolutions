# Leetode 2800: Shortest String That Contains Three Strings
# https://leetcode.com/problems/shortest-string-that-contains-three-strings/
# Solved on 7th of January, 2026
import itertools


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        """
        Finds the lexicographically smallest shortest string that contains all three input strings.

        Args:
            a (str): The first input string.
            b (str): The second input string.
            c (str): The third input string.

        Returns:
            str: The lexicographically smallest shortest string containing a, b, and c.
        """
        def merge(s1, s2):
            if s2 in s1:
                return s1
            for i in range(min(len(s1), len(s2)), -1, -1):
                if s1.endswith(s2[:i]):
                    return s1 + s2[i:]

            return s1 + s2

        minStr = ""
        minLen = float('inf')

        for p in itertools.permutations([a, b, c]):
            currentStr = merge(p[0], p[1])
            currentStr = merge(currentStr, p[2])

            if len(currentStr) < minLen:
                minStr = currentStr
                minLen = len(currentStr)
            elif len(currentStr) == minLen:
                if currentStr < minStr:
                    minStr = currentStr

        return minStr