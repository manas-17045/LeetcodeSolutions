# Leetcode 865: Smallest Subtree with all the Deepest Nodes
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# Solved on 9th of January, 2026
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Finds the smallest subtree that contains all the deepest nodes.

        Args:
            root: The root of the binary tree.

        Returns:
            The root of the smallest subtree containing all deepest nodes.
        """
        def dfs(node):
            if not node:
                return 0, None

            leftDepth, leftNode = dfs(node.left)
            rightDepth, rightNode = dfs(node.right)

            if leftDepth > rightDepth:
                return leftDepth + 1, leftNode
            elif rightDepth > leftDepth:
                return rightDepth + 1, rightNode
            else:
                return leftDepth + 1, node

        return dfs(root)[1]