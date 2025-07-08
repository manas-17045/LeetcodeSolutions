# Leetcode 1147: Longest Chunked Palindrome Decomposition
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
# Solved on 8th of July, 2025
class Solution:
    def longestDecomposition(self, text: str) -> int:
        """
        Calculates the longest decomposition of a string into palindromic chunks.

        Args:
            text: The input string.

        Returns:
            The maximum number of chunks in the decomposition.
        """
        n = len(text)
        l, r = 0, (n - 1)
        count = 0

        # While there is still some (possibly overlapping) substring left
        while l <= r:
            # Try all possible chunk-lengths k from 1 up to half the remaining window
            matched = False
            # Max chunk size is (r - l + 1) // 2
            max_k = (r - l + 1) // 2
            for k in range(1, max_k + 1):
                if text[l:l + k] == text[r - k + 1:r + 1]:
                    count += 2
                    l += k
                    r -= k
                    matched = True
                    break

            if not matched:
                # No more matching chunks => the rest is one middle chunk
                count += 1
                break

        return count