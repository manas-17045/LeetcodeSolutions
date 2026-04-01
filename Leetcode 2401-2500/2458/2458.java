// Leetcode 2458: Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
// Solved on 1st of April, 2026
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
    int currentMax;
    int[] maxDepth;
    
    /**
     * Calculates the height of the binary tree after removing specific subtrees.
     * 
     * @param root The root of the binary tree.
     * @param queries An array of node values representing the subtrees to be removed.
     * @return An array of integers representing the tree height after each query.
     */
    public int treeQueries(TreeNode root, int[] queries) {
        maxDepth = new int[100001];
        currentMax = 0;
        traverseLeft(root, 0);
        currentMax = 0;
        traverseRight(root, 0);
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            result[i] = maxDepth[queries[i]];
        }
        return result;
    }

    private void traverseLeft(TreeNode node, int depth) {
        if (node == null) {
            return;
        }
        maxDepth[node.val] = currentMax;
        currentMax = Math.max(currentMax, depth);
        traverseLeft(node.left, depth + 1);
        traverseLeft(node.right, depth + 1);
    }

    private void traverseRight(TreeNode node, int depth) {
        if (node == null) {
            return;
        }
        maxDepth[node.val] = Math.max(maxDepth[node.val], currentMax);
        currentMax = Math.max(currentMax, depth);
        traverseRight(node.right, depth + 1);
        traverseRight(node.left, depth + 1);
    }
}