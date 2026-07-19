# Leetcode 1081: Smallest Subsequence of Distinct Characters
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters
# Solved on 19th of July, 2026
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """
        Finds the lexicographically smallest subsequence of distinct characters.
        
        Args:
            s: The input string.
            
        Returns:
            The lexicographically smallest subsequence of distinct characters.
        """
        lastOccurrence = {}
        for i, currentChar in enumerate(s):
            lastOccurrence[currentChar] = i

        seenChars = set()
        charStack = []

        for i, currentChar in enumerate(s):
            if currentChar not in seenChars:
                while charStack and charStack[-1] > currentChar and lastOccurrence[charStack[-1]] > i:
                    seenChars.remove(charStack.pop())
                charStack.append(currentChar)
                seenChars.add(currentChar)
        
        return "".join(charStack)