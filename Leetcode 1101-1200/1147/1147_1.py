# Leetcode 1147: Longest Chunked Palindrome Decomposition
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
# Solved on 8th of July, 2025
class Solution:
    def longestDecomposition(self, text: str) -> int:
        """
        Calculates the longest chunked palindrome decomposition of a given string.

        Args:
            text: The input string.
        """
        chunkCount = 0
        textLen = len(text)
        left = 0
        right = textLen

        while left < right:
            matchFound = False
            remainingLen = right - left

            for chunkLen in range(1, remainingLen // 2 + 1):
                if text[left:left + chunkLen] == text[right - chunkLen:right]:
                    chunkCount += 2
                    left += chunkLen
                    right -= chunkLen
                    matchFound = True
                    break

            if not matchFound:
                chunkCount += 1
                break

        return chunkCount