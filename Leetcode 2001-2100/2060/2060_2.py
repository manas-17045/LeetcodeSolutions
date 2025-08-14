# Leetcode 2060: Check If an Original String Exists Given Two Encoded Strings
# https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/
# Solved on 14th of August, 2025
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        """
        Determines if two strings s1 and s2 can be considered "possibly equal" based on specific rules.

        Args:
            s1 (str): The first string.
            s2 (str): The second string.
        Returns:
            bool: True if the strings can be possibly equal, False otherwise.
        """
        n1, n2 = len(s1), len(s2)

        @lru_cache(None)
        def dfs(i: int, j: int, diff: int) -> bool:
            if i == n1 and j == n2:
                return diff == 0

            if diff > 0:
                if j < n2 and s2[j].isalpha():
                    if dfs(i, j + 1, diff - 1):
                        return True

                if j < n2 and s2[j].isdigit():
                    num = 0
                    for k in range(j, min(j + 3, n2)):
                        if not s2[k].isdigit():
                            break
                        num = num * 10 + (ord(s2[k]) - 48)
                        if dfs(i, k + 1, diff - num):
                            return True

                return False

            if diff < 0:
                if i < n1 and s1[i].isalpha():
                    if dfs(i + 1, j, diff + 1):
                        return True

                if i < n1 and s1[i].isdigit():
                    num = 0
                    for k in range(i, min(i + 3, n1)):
                        if not s1[k].isdigit():
                            break
                        num = num * 10 + (ord(s1[k]) - 48)
                        if dfs(k + 1, j, diff + num):
                            return True

                return False

            if i < n1 and j < n2 and s1[i].isalpha() and s2[j].isalpha():
                if s1[i] == s2[j] and dfs(i + 1, j + 1, 0):
                    return True

            if i < n1 and s1[i].isdigit():
                num = 0
                for k in range(i, min(i + 3, n1)):
                    if not s1[k].isdigit():
                        break
                    num = num * 10 + (ord(s1[k]) - 48)
                    if dfs(k + 1, j, num):
                        return True

            if j < n2 and s2[j].isdigit():
                num = 0
                for k in range(j, min(j + 3, n2)):
                    if not s2[k].isdigit():
                        break
                    num = num * 10 + (ord(s2[k]) - 48)
                    if dfs(i, k + 1, -num):
                        return True

            return False

        return dfs(0, 0, 0)