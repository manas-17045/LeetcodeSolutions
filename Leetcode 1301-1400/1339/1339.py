# Leetcode 1339: Maximum Product of Splitted Binary Tree
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
# Solved on 7th of January, 2026
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, split the binary tree into two subtrees by removing one edge
        such that the product of the sums of the subtrees is maximized.

        :param root: The root of the binary tree.
        :return: The maximum product of the sums of the two subtrees modulo 10^9 + 7.
        """
        subtreeSums = []

        def calculateSum(node):
            if not node:
                return 0
            currentSum = node.val + calculateSum(node.left) + calculateSum(node.right)
            subtreeSums.append(currentSum)
            return currentSum

        totalSum = calculateSum(root)
        maxProduct = 0

        for s in subtreeSums:
            product = s * (totalSum - s)
            if product > maxProduct:
                maxProduct = product

        return maxProduct % (10 ** 9 + 7)