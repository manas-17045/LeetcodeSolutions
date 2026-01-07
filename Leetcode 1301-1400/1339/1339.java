// Leetcode 1339: Maximum Product of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
// Solved on 7th of January, 2026
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
    long totalSum = 0;
    long maxResult = 0;

    /**
     * Calculates the maximum product of the sums of two subtrees after splitting the original tree.
     * @param root The root of the binary tree.
     * @return The maximum product modulo 10^9 + 7.
     */
    public int maxProduct(TreeNode root) {
        totalSum = 0;
        maxResult = 0;
        totalSum = calculateSubtreeSum(root);
        calculateSubtreeSum(root);
        return (int) (maxResult % 1000000007);
    }

    long calculateSubtreeSum(TreeNode node) {
        if (node == null) {
            return 0;
        }
        long currentSum = node.val + calculateSubtreeSum(node.left) + calculateSubtreeSum(node.right);
        long currentProduct = currentSum * (totalSum - currentSum);
        if (currentProduct > maxResult) {
            maxResult = currentProduct;
        }
        return currentSum;
    }
}