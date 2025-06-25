# Leetcode 2003: Smallest Missing Genetic Value in Each Subtree
# https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/
# Solved on 25th of June, 2025
import collections


class Solution:
    def smallestMissingvalueSubtree(self, parents: list[int], nums: list[int]) -> list[int]:
        n = len(parents)
        adj = collections.defaultdict(list)
        for i, parentNode in enumerate(parents):
            if parentNode != -1:
                adj[parentNode].append(i)

        ans = [1] * n

        nodeOneIndex = -1
        for i in range(n):
            if nums[i] == 1:
                nodeOneIndex = i
                break

        if nodeOneIndex == -1:
            return ans

        pathValues = set()
        currntMissingValue = 1

        currentNodeOnPath = nodeOneIndex
        previousNodeOnPath = -1

        while currentNodeOnPath != -1:
            pathValues.add(nums[currentNodeOnPath])

            for childNode in adj[currentNodeOnPath]:
                if childNode != previousNodeOnPath:
                    # Iterative DFS for the side branch rooted at childNode
                    iterationStack = [childNode]
                    while iterationStack:
                        nodeToProcess = iterationStack.pop()
                        pathValues.add(nums[nodeToProcess])
                        for neighborNode in adj[nodeToProcess]:
                            iterationStack.append(neighborNode)

            while currntMissingValue in pathValues:
                currntMissingValue += 1
            ans[currentNodeOnPath] = currntMissingValue

            previousNodeOnPath = currentNodeOnPath
            currentNodeOnPath = parents[currentNodeOnPath]

        return ans