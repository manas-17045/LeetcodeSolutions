# Leetcode 2157: Groups of Strings
# https://leetcode.com/problems/groups-of-strings/
# Solved on 9th of July, 2025
import collections


class Solution:
    def groupStrings(self, words: list[str]) -> list[int]:
        """
        This function groups strings based on their character masks and
        determines the number of distinct groups and the maximum size among them.
        Two strings are in the same group if one can be transformed into the other
        by adding or deleting a single character, or by replacing a single character.
        This is achieved by using a Disjoint Set Union (DSU) data structure
        to manage the groups of character masks.

        :param words: A list of strings.
        :return: A list containing two integers: the number of groups and the maximum group size.
        """

        class DSU:
            def __init__(self, items):
                self.parent = {item: item for item in items}
                self.groupSize = {}

            def find(self, i):
                if self.parent[i] == i:
                    return i
                self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, i, j):
                rootI = self.find(i)
                rootJ = self.find(j)
                if rootI != rootJ:
                    if self.groupSize[rootI] < self.groupSize[rootJ]:
                        rootI, rootJ = rootJ, rootI
                    self.parent[rootJ] = rootI
                    self.groupSize[rootI] += self.groupSize[rootJ]

        masksCounts = collections.Counter()
        for word in words:
            mask = 0
            for char in word:
                mask |= (1 << (ord(char) - ord('a')))
            masksCounts[mask] += 1

        uniqueMasks = list(masksCounts.keys())
        dsu = DSU(uniqueMasks)
        for mask in uniqueMasks:
            dsu.groupSize[mask] = masksCounts[mask]

        deletedMap = {}
        for mask in uniqueMasks:
            for i in range(26):
                neighbor = mask ^ (1 << i)
                if neighbor in dsu.parent:
                    if neighbor > mask:
                        dsu.union(mask, neighbor)

            for i in range(26):
                if (mask >> i) & 1:
                    deletedMask = mask ^ (1 << i)
                    if deletedMask in deletedMap:
                        dsu.union(mask, deletedMap[deletedMask])
                    else:
                        deletedMap[deletedMask] = mask

        numGroups = 0
        maxGroupSize = 0
        visitedRoots = set()
        for mask in uniqueMasks:
            root = dsu.find(mask)
            if root not in visitedRoots:
                numGroups += 1
                maxGroupSize = max(maxGroupSize, dsu.groupSize[root])
                visitedRoots.add(root)

        return [numGroups, maxGroupSize]