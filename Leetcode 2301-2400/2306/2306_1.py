# Leetcode 2306: Naming a Company
# https://leetcode.com/problems/naming-a-company/
# Solved on 21st of June, 2025
from collections import defaultdict


class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        """
        Calculates the number of distinct company names that can be formed.

        A distinct company name can be formed by taking two existing ideas,
        swapping their first letters, and ensuring both resulting words are not
        already present in the original list of ideas.

        Args:
            ideas: A list of strings representing existing company ideas.
        Returns:
            The total count of distinct company names that can be formed.
        """
        suffixGroups = defaultdict(list)
        for idea in ideas:
            suffixGroups[idea[0]].append(idea[1:])

        distinctNamesCount = 0

        for i in range(26):
            char1 = chr(ord('a') + i)
            group1Suffixes = suffixGroups[char1]

            if not group1Suffixes:
                continue

            for j in range(26):
                if i == j:
                    continue

                char2 = chr(ord('a') + j)
                group2Suffixes = suffixGroups[char2]

                if not group2Suffixes:
                    continue

                numCommonSuffixes = 0
                if len(group1Suffixes) <= len(group2Suffixes):
                    for suffix in group1Suffixes:
                        if suffix in group2Suffixes:
                            numCommonSuffixes += 1
                else:
                    for suffix in group2Suffixes:
                        if suffix in group1Suffixes:
                            numCommonSuffixes += 1

                exclusiveToGroup1 = len(group1Suffixes) - numCommonSuffixes
                exclusiveToGroup2 = len(group2Suffixes) - numCommonSuffixes

                distinctNamesCount += exclusiveToGroup1 * exclusiveToGroup2

        return distinctNamesCount