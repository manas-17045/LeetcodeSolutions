# Leetcode 2734: Lexicographically Smallest String After Substring Operation
# https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/
# Solved on 18th of June, 2025

class Solution:
    def smallestString(self, s: str) -> str:
        """
        Given a string s, you are allowed to perform one operation: choose a non-empty substring
        and decrease the alphabetical value of each character in the substring by one.
        For example, 'c' becomes 'b', 'b' becomes 'a', and 'a' becomes 'z'.
        Return the lexicographically smallest string you can obtain after performing exactly one operation.

        Args:
            s: The input string.
        Returns:
            The lexicographically smallest string after one operation.
        """
        n = len(s)
        stringChars = list(s)

        firstNonA = 0
        while firstNonA < n and stringChars[firstNonA] == 'a':
            firstNonA += 1

        if firstNonA == n:
            stringChars[n - 1] = 'z'
            return "".join(stringChars)

        endOfNonASegment = firstNonA
        while endOfNonASegment < n and stringChars[endOfNonASegment] != 'a':
            endOfNonASegment += 1

        for i in range(firstNonA, endOfNonASegment):
            stringChars[i] = chr(ord(stringChars[i]) - 1)

        return "".join(stringChars)