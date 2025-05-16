# Leetcode 2901: Longest Unequal Adjacent Groups Subsequence II
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/
# Solved on 16th of May, 2025

class Solution:
    def getWordsInLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        """
        Finds the longest subsequence of words where adjacent words have different groups and a Hamming distance of 1.

        Args:
            words: A list of strings representing the words.
            groups: A list of integers representing the group each word belongs to.

        Returns:
            A list of strings representing the longest subsequence satisfying the conditions.
        """
        n = len(words)
        # dp[i]: length of longest valid subsequence ending at i
        dp = [1] * n
        # parent pointers to reconstruct path
        parent = [-1] * n

        best_len = 1
        best_end = 0

        # Helper to check hamming distance == 1 and equal length
        def is_hamming1(a: str, b: str) -> bool:
            # lengths are equal by caller
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        # Build dp
        for i in range(n):
            for j in range(i):
                # Adjacent criteria: group differ, same length, hamming distance == 1
                if groups[j] != groups[i] and len(words[j]) == len(words[i]) and is_hamming1(words[j], words[i]):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            # Track global best
            if dp[i] > best_len:
                best_len = dp[i]
                best_end = i

        # Reconstruct from best_end backwards
        res = []
        cur = best_end
        while cur != -1:
            res.append(words[cur])
            cur = parent[cur]
        res.reverse()
        return res