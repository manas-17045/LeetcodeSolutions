# Leetcode 3839: Number of Prefix Connected Groups
# https://leetcode.com/problems/number-of-prefix-connected-groups/
# Solved on 16th of February, 2026
class Solution:
    def prefixConnected(self, words: list[str], k: int) -> int:
        """
        Calculates the number of groups where at least two words share the same prefix of length k.

        :param words: A list of strings to evaluate.
        :param k: The required length of the prefix to be considered for grouping.
        :return: The total count of unique prefixes of length k that appear in at least two words.
        """
        prefixCounts = {}
        for currentWord in words:
            if len(currentWord) >= k:
                currentPrefix = currentWord[:k]
                prefixCounts[currentPrefix] = prefixCounts.get(currentPrefix, 0) + 1

        totalGroups = 0
        for countValue in prefixCounts.values():
            if countValue >= 2:
                totalGroups += 1

        return totalGroups