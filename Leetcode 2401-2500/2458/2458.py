# Leetcode 2458: Height of Binary Tree After Subtree Removal Queries
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
# Solved on 1st of April, 2026
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: list[int]) -> list[int]:
        """
        Calculates the maximum height of the binary tree after removing a specified subtree for each query.

        :param root: The root of the binary tree.
        :param queries: A list of node values representing the roots of subtrees to be removed.
        :return: A list of integers representing the tree height after each removal query.
        """
        removalHeights = [0] * 100005
        self.currentMax = 0

        def traverseLeft(currentNode, currentDepth):
            if not currentNode:
                return

            removalHeights[currentNode.val] = self.currentMax
            if currentDepth > self.currentMax:
                self.currentMax = currentDepth

            traverseLeft(currentNode.left, currentDepth + 1)
            traverseLeft(currentNode.right, currentDepth + 1)

        def traverseRight(currentNode, currentDepth):
            if not currentNode:
                return

            if self.currentMax > removalHeights[currentNode.val]:
                removalHeights[currentNode.val] = self.currentMax
            if currentDepth > self.currentMax:
                self.currentMax = currentDepth

            traverseRight(currentNode.right, currentDepth + 1)
            traverseRight(currentNode.left, currentDepth + 1)

        traverseLeft(root, 0)
        self.currentMax = 0
        traverseRight(root, 0)

        resultArray = []
        for queryNodeVal in queries:
            resultArray.append(removalHeights[queryNodeVal])

        return resultArray