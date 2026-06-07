# Leetcode 2196: Create Binary Tree From Descriptions
# https://leetcode.com/problems/create-binary-tree-from-descriptions/
# Solved on 7th of June, 2026
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        """
        Creates a binary tree from a 2D array of descriptions.

        :param descriptions: A list of [parent, child, isLeft] where isLeft is 1 if child is left, 0 otherwise.
        :return: The root node of the constructed binary tree.
        """
        nodesMap = {}
        allChildren = set()

        for parentVal, childVal, isLeft in descriptions:
            if parentVal not in nodesMap:
                nodesMap[parentVal] = TreeNode(parentVal)
            if childVal not in nodesMap:
                nodesMap[childVal] = TreeNode(childVal)

            if isLeft:
                nodesMap[parentVal].left = nodesMap[childVal]
            else:
                nodesMap[parentVal].right = nodesMap[childVal]

            allChildren.add(childVal)

        for parentVal in nodesMap:
            if parentVal not in allChildren:
                return nodesMap[parentVal]