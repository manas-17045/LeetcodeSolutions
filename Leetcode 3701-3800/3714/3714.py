# Leetcode 3714: Longest Balanced Substring II
# https://leetcode.com/problems/longest-balanced-substring-ii/
# Solved on 4th of November, 2025
class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        Finds the length of the longest balanced substring in a given string.

        Args:
            s (str): The input string consisting of characters 'a', 'b', and 'c'.
        Returns:
            int: The length of the longest balanced substring.
        """
        maxLength = 0

        def solveOne(c1, c2, c3):
            length = 0
            currentLength = 0
            for char in s:
                if char == c1:
                    currentLength += 1
                elif char == c2 or char == c3:
                    length = max(length, currentLength)
                    currentLength = 0
            length = max(length, currentLength)
            return length

        def solveTwo(c1, c2, c3):
            counts = {c1: 0, c2: 0}
            seen = {0: -1}
            length = 0
            for i, char in enumerate(s):
                if char == c1:
                    counts[c1] += 1
                elif char == c2:
                    counts[c2] += 1
                elif char == c3:
                    counts = {c1: 0, c2: 0}
                    seen = {0: i}
                    continue
                else:
                    continue

                diff = counts[c1] - counts[c2]
                if diff in seen:
                    length = max(length, i - seen[diff])
                else:
                    seen[diff] = i
            return length

        def solveThree():
            seen = {(0, 0): -1}
            length = 0
            countA = 0
            countB = 0
            countC = 0
            for i, char in enumerate(s):
                if char == 'a':
                    countA += 1
                elif char == 'b':
                    countB += 1
                elif char == 'c':
                    countC += 1

                key = (countA - countB, countB - countC)

                if key in seen:
                    length = max(length, i - seen[key])
                else:
                    seen[key] = i
            return length

        maxLength = max(maxLength, solveOne('a', 'b', 'c'))
        maxLength = max(maxLength, solveOne('b', 'a', 'c'))
        maxLength = max(maxLength, solveOne('c', 'a', 'b'))
        maxLength = max(maxLength, solveTwo('a', 'b', 'c'))
        maxLength = max(maxLength, solveTwo('a', 'c', 'b'))
        maxLength = max(maxLength, solveTwo('b', 'c', 'a'))
        maxLength = max(maxLength, solveThree())

        return maxLength