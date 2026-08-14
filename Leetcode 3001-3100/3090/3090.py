# Leetcode 3090: Maximum Length Substring With Two Occurrences
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
# Solved on 14th of August, 2026
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        """
        Computes the maximum length of a substring of s that contains at most two occurrences of each character.
        
        Args:
            s: The input string.
            
        Returns:
            The maximum length of the substring.
        """
        charFrequency = {}
        maxLength = 0
        leftIndex = 0

        for rightIndex, currentChar in enumerate(s):
            charFrequency[currentChar] = charFrequency.get(currentChar, 0) + 1

            while charFrequency[currentChar] > 2:
                charFrequency[s[leftIndex]] -= 1
                leftIndex += 1

            maxLength = max(maxLength, rightIndex - leftIndex + 1)

        return maxLength