# Leetcode 1022: Sum of Root To Leaf Binary Numbers
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Solved on 24th of February, 2026
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the sum of all numbers represented by root-to-leaf paths in a binary tree.
        Each path represents a binary number where the root is the most significant bit.
        :param root: The root of the binary tree containing values 0 or 1.
        :return: The total sum of all root-to-leaf binary numbers.
        """
        def calculateSum(currentNode, currentSum):
            if not currentNode:
                return 0

            currentSum = (currentSum << 1) | currentNode.val

            if not currentNode.left and not currentNode.right:
                return currentSum

            return calculateSum(currentNode.left, currentSum) + calculateSum(currentNode.right, currentSum)

        return calculateSum(root, 0)