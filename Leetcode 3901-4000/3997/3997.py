# Leetcode 3997: Count Dominant Nodes in a Binary Tree
# https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/
# Solved on 19th of August, 2026
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        """
        Counts the total number of dominant nodes in a binary tree where a node's 
        value is greater than or equal to all values in its subtree.

        Parameters:
            root (TreeNode | None): The root node of the binary tree.

        Returns:
            int: The total count of dominant nodes in the tree.
        """
        dominantCount = 0

        def traverseTree(currentNode: TreeNode | None) -> int:
            nonlocal dominantCount
            if not currentNode:
                return 0

            leftMax = traverseTree(currentNode.left)
            rightMax = traverseTree(currentNode.right)
            currentMax = max(currentNode.val, leftMax, rightMax)

            if currentNode.val == currentMax:
                dominantCount += 1

            return currentMax

        traverseTree(root)
        return dominantCount