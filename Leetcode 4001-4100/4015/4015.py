# Leetcode 4015: Weighted Sum of a Tree
# https://leetcode.com/problems/weighted-sum-of-a-tree/
# Solved on 7th of September, 2026
class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        """
        Calculates the sum of the weights of all nodes in a rooted tree.

        Parameters:
            parent (list[int]): An array where parent[i] denotes the parent of node i.
            nums (list[int]): An array where nums[i] denotes the value of node i.

        Returns:
            int: The total weighted sum of all nodes in the tree.
        """
        numNodes = len(parent)
        treeChildren = [[] for _ in range(numNodes)]

        for childNode in range(1, numNodes):
            treeChildren[parent[childNode]].append(childNode)

        currentLevel = [0]
        levelSums = []

        while currentLevel:
            currentSum = 0
            nextLevel = []
            for currentNode in currentLevel:
                currentSum += nums[currentNode]
                nextLevel.extend(treeChildren[currentNode])
            levelSums.append(currentSum)
            currentLevel = nextLevel

        totalHeight = len(levelSums)
        totalWeight = 0

        for levelIndex in range(totalHeight):
            totalWeight += levelSums[levelIndex] * (totalWeight - levelIndex)

        return totalWeight