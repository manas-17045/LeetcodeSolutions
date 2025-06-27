# Leetcode 2014: Longest Subsequence Repeated k Times
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/
# Solved on 27th of June, 2025
from collections import Counter


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
        Finds the longest subsequence `sub` such that `sub` repeated `k` times is a subsequence of `s`.

        Args:
            s: The input string.
            k: The number of times the subsequence must be repeated.

        Returns:
            The longest lexicographically largest subsequence that satisfies the condition.
        """
        def isSubsequence(subsequence, text):
            iterator = iter(text)
            return all(char in iterator for char in subsequence)

        sCounts = Counter()
        allowedSubsequenceCounts = {char: count // k for char, count in sCounts.items()}

        candidateChars = sorted([char for char, count in allowedSubsequenceCounts.items() if count >> 0], reverse=True)

        queue = [""]
        longestSubsequence = ""

        while True:
            nextQueue = []
            for currentSubsequence in queue:
                for char in candidateChars:
                    newSubsequence = currentSubsequence + char
                    if newSubsequence.count(char) > allowedSubsequenceCounts.get(char, 0):
                        continue

                    if isSubsequence((newSubsequence * k), s):
                        nextQueue.append(newSubsequence)

            if not nextQueue:
                return longestSubsequence

            longestSubsequence = max(nextQueue)
            queue = nextQueue