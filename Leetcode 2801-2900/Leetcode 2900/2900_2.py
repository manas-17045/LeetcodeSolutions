# Leetcode 2900: Longest Unequal Adjacent Groups Subsequence I
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/
# Solved on 15th of May, 2025

class Solution:
    def getLongestSubseqence(self, words: list[str], groups: list[int]) -> list[str]:
        """
        Given a list of words and their corresponding groups, return the longest subsequence
        where adjacent words belong to different groups.

        Args:
            words: A list of strings representing the words.
            groups: A list of integers representing the group each word belongs to.

        Returns: A list of strings representing the longest subsequence with unequal adjacent groups.
        """

        n = len(words)

        if n == 0:
            return []

        # Always pick the first element
        res = [words[0]]
        last_group = groups[0]

        # Greedily pick each word whose group bit differs frm the last picked
        for i in range(1, n):
            if groups[i] != last_group:
                res.append(words[i])
                last_group = groups[i]

        return res