# Leetcode 1161: Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Solved on 6th of January, 2026
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the level with the maximum sum in a binary tree.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: The level number (1-indexed) with the maximum sum.
        """
        maxSum = float('-inf')
        resultLevel = 0
        currentLevel = 1
        queue = collections.deque([root])

        while queue:
            currentSum = 0
            levelSize = len(queue)

            for _ in range(levelSize):
                node = queue.popleft()
                currentSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if currentSum > maxSum:
                maxSum = currentSum
                resultLevel = currentLevel

            currentLevel += 1

        return resultLevel