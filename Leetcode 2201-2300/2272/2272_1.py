# Leetcode 2272: Substrings With Largest Variance
# https://leetcode.com/problems/substrings-with-largest-variance/
# Solved on 9th of July, 2025
class Solution:
    def largestVariance(self, s: str) -> int:
        """
        Calculates the largest variance of any substring in `s`.
        The variance of a substring is defined as the maximum difference
        between the count of one character (majorChar) and another character (minorChar).

        Args:
            s: The input string.

        Returns:
            The largest variance found.
        """
        uniqueChars = sorted(list(set(s)))
        maxVariance = 0

        for majorChar in uniqueChars:
            for minorChar in uniqueChars:
                if majorChar == minorChar:
                    continue

                # Kadane's algorithm variant
                currentVariance = 0
                hasMajor = False
                hasMinor = False

                for i in range(2):
                    if i == 1:
                        s = s[::-1]

                    currentVariance = 0
                    hasMajor = False
                    hasMinor = False

                    for char in s:
                        if char == majorChar:
                            currentVariance += 1
                            hasMajor = True
                        elif char == minorChar:
                            currentVariance -= 1
                            hasMinor = True

                        # A valid substring must contain both characters.
                        if hasMajor and hasMinor:
                            maxVariance = max(maxVariance, currentVariance)

                        if currentVariance < 0:
                            currentVariance = 0
                            hasMajor = False
                            hasMinor = False

        return maxVariance