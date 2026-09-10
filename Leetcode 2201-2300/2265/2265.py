# Leetcode 2265: Count Nodes Equal to Average of Subtree
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
# Solved on 10th of September, 2026
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        """
        Calculates the number of nodes equal to the average of their subtree.

        Parameters:
            root (TreeNode): The root of the binary tree.

        Returns:
            int: The number of nodes where the node value equals the subtree average.
        """
        totalMatches, _, _ = self.evaluateSubtree(root)
        return totalMatches

    def evaluateSubtree(self, currNode: TreeNode) -> tuple[int, int, int]:
        if not currNode:
            return 0, 0, 0

        leftMatches, leftSum, leftCount = self.evaluateSubtree(currNode.left)
        rightMatches, rightSum, rightCount = self.evaluateSubtree(currNode.right)

        totalSum = currNode.val + leftSum + rightSum
        totalCount = 1 + leftCount + rightCount
        nodeMatch = 1 if currNode.val == totalSum // totalCount else 0

        totalMatches = leftMatches + rightMatches + nodeMatch

        return totalMatches, totalSum, totalCount