# Leetcode 3863: Minimum Operations to Sort a String
# https://leetcode.com/problems/minimum-operations-to-sort-a-string/
# Solved on 10th of March, 2026
class Solution:
    def minOperations(self, s: str) -> int:
        """
        Calculates the minimum number of operations required to sort a string.

        Args:
            s (str): The input string to be sorted.
        Returns:
            int: The minimum number of operations, or -1 if it's impossible.
        """
        n = len(s)

        isSorted = True
        for i in range(1, n):
            if s[i] < s[i - 1]:
                isSorted = False
                break

        if isSorted:
            return 0

        if n == 2:
            return -1

        minChar = min(s)
        maxChar = max(s)

        if s[0] == minChar or s[-1] == maxChar:
            return 1

        if s[0] == maxChar and s[-1] == minChar and s.count(maxChar) == 1 and s.count(minChar) == 1:
            return 3

        return 2