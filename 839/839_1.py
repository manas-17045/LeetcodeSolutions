# Leetcode 839: Similar String Groups
# https://leetcode.com/problems/similar-string-groups/
# Solved on 9th of July, 2025
class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        """
        Calculates the number of similar string groups.

        Two strings are similar if they are the same or if they can be made the same
        by swapping exactly two characters in one of the strings.
        This problem uses a Union-Find data structure to group similar strings.
        """
        n = len(strs)
        parent = list(range(n))
        numGroups = n

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            nonlocal numGroups
            rootI = find(i)
            rootJ = find(j)
            if rootI != rootJ:
                parent[rootJ] = rootI
                numGroups -= 1

        def areSimilar(s1, s2):
            diffCount = 0
            for k in range(len(s1)):
                if s1[k] != s2[k]:
                    diffCount += 1
            return diffCount == 2 or diffCount == 0

        for i in range(n):
            for j in range((i + 1), n):
                if areSimilar(strs[i], strs[j]):
                    union(i, j)

        return numGroups