// Leetcode 3997: Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/
// Solved on 19th of August, 2026
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
    private int dominantCount = 0;

    /**
     * Counts the total number of dominant nodes in a binary tree.
     * A node is considered dominant if its value is greater than or equal
     * to all node values in its subtree.
     *
     * @param root the root node of the binary tree
     * @return the total count of dominant nodes
     */
    public int countDominantNodes(TreeNode root) {
        dominantCount = 0;
        findSubtreeMax(root);
        return dominantCount;
    }

    private int findSubtreeMax(TreeNode node) {
        if (node == null) {
            return Integer.MIN_VALUE;
        }

        int leftMax = findSubtreeMax(node.left);
        int rightMax = findSubtreeMax(node.right);

        int maxVal = Math.max(node.val, Math.max(leftMax, rightMax));

        if (node.val == maxVal) {
            dominantCount++;
        }

        return maxVal;
    }
}