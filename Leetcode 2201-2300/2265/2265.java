// Leetcode 2265: Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
// Solved on 10th of September, 2026
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private int matchingNodeCount;

    /**
     * Calculates the number of nodes in a binary tree where the node's value
     * is equal to the floor average of the values in its subtree.
     *
     * @param root the root node of the binary tree
     * @return the total number of nodes matching the subtree average condition
     */
    private int averageOfSubtree(TreeNode root) {
        matchingNodeCount = 0;
        traverseSubtree(root);
        return matchingNodeCount;
    }

    private int[] traverseSubtree(TreeNode currentNode) {
        if (currentNode == null) {
            return new int[]{0, 0};
        }

        int[] leftResult = traverseSubtree(currentNode.left);
        int[] rightResult = traverseSubtree(currentNode.right);

        int subtreeSum = leftResult[0] + rightResult[0] + currentNode.val;
        int subtreeCount = leftResult[1] + rightResult[1] + 1;

        if (currentNode.val == subtreeSum / subtreeCount) {
            matchingNodeCount++;
        }

        return new int[]{subtreeSum, subtreeCount};
    }
}