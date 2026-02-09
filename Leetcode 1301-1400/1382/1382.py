# Leetcode 1382: Balance a Binary Search Tree
# https://leetcode.com/problems/balance-a-binary-search-tree/
# Solved on 9th of February, 2026
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Converts a given binary search tree into a balanced binary search tree.

        :param root: The root of the original binary search tree.
        :return: The root of a new, balanced binary search tree.
        """
        sortedNodes = []

        def inOrderTraversal(node):
            if node is None:
                return
            inOrderTraversal(node.left)
            sortedNodes.append(node)
            inOrderTraversal(node.right)

        inOrderTraversal(root)

        def constructBalancedTree(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            newRoot = sortedNodes[mid]
            newRoot.left = constructBalancedTree(start, mid - 1)
            newRoot.right = constructBalancedTree(mid + 1, end)
            return newRoot

        return constructBalancedTree(0, len(sortedNodes) - 1)