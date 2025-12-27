# Leetcode 3722: Lexicographically Smallest String After Reverse
# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/
# Solved on 27th of December, 2025
class Solution:
    def lesSmallest(self, s: str) -> str:
        """
        Finds the lexicographically smallest string after performing at most one reverse operation.

        Args:
            s (str): The input string.
        Returns:
            str: The lexicographically smallest string.
        """
        n = len(s)
        minStr = None
        for k in range(1, n + 1):
            preRev = s[:k][::-1] + s[k:]
            if minStr is None or preRev < minStr:
                minStr = preRev

            sufRev = s[:n - k] + s[n - k:][::-1]
            if sufRev < minStr:
                minStr = sufRev

        return minStr