# Leetcode 3170: Lexicographically Minimum String After Removing Stars
# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/
# Solved on 7th of June, 2025

class Solution:
    def clearStars(self, s: str) -> str:
        """
        Given a string s, remove stars such that the resulting string is lexicographically smallest.
        When a star is encountered, remove the lexicographically smallest character to its left.
        If there are multiple such characters, remove the rightmost one.

        Args:
            s: The input string.

        Returns:
            The lexicographically smallest string after removing stars.
        """
        n = len(s)
        charPositions = [[] for _ in range(26)]
        removed = [False] * n

        for i, char in enumerate(s):
            if char == '*':
                removed[i] = True
                for j in range(26):
                    if charPositions[j]:
                        idxToRemove = charPositions[j].pop()
                        removed[idxToRemove] = True
                        break
            else:
                charIdx = ord(char) - ord('a')
                charPositions[charIdx].append(i)

        res = []
        for i in range(n):
            if not removed[i]:
                res.append(s[i])

        return "".join(res)