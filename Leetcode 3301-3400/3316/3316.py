# Leetcode 3316: Find Maximum Removals From Sources String
# https://leetcode.com/problems/find-maximum-removals-from-source-string/
# Solved on 7th of December, 2025
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: list[int]) -> int:
        """
        Finds the maximum number of characters that can be removed from the source string
        such that the pattern string can still be formed as a subsequence.
        :param source: The source string.
        :param pattern: The pattern string.
        :param targetIndices: A list of indices in the source string that can be removed.
        :return: The maximum number of removable characters.
        """
        sourceLength = len(source)
        patternLength = len(pattern)

        isTarget = [False] * sourceLength
        for index in targetIndices:
            isTarget[index] = True

        dp = [float('inf')] * (patternLength + 1)
        dp[0] = 0

        patternMap = [[] for _ in range(26)]
        for i, char in enumerate(pattern):
            patternMap[ord(char) - 97].append(i)

        for indices in patternMap:
            indices.reverse()

        for i, char in enumerate(source):
            currentCost = 1 if isTarget[i] else 0
            charCode = ord(char) - 97

            for j in patternMap[charCode]:
                if dp[j] != float('inf'):
                    newCost = dp[j] + currentCost
                    if newCost < dp[j + 1]:
                        dp[j + 1] = newCost

        return int(len(targetIndices) - dp[patternLength])