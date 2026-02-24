// Leetcode 1022: Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
// Solved on 24th of February, 2026
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
    /**
     * Calculates the sum of all numbers formed by root-to-leaf paths in a binary tree.
     * @param root The root of the binary tree where each node contains a 0 or 1.
     * @return The total sum of all binary numbers represented by the paths.
     */
    public int sumRootToLeaf(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int currentSum) {
        if (node == null) {
            return 0;
        }
        currentSum = (currentSum << 1) | node.val;
        if (node.left == null && node.right == null) {
            return currentSum;
        }
        return dfs(node.left, currentSum) + dfs(node.right, currentSum);
    }
}