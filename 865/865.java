// Leetcode 865: Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
// Solved on 9th of January, 2026
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
    class NodeData {
        TreeNode node;
        int depth;

        NodeData(TreeNode node, int depth) {
            this.node = node;
            this.depth = depth;
        }
    }

    /**
     * Finds the smallest subtree that contains all the deepest nodes.
     * @param root The root of the binary tree.
     * @return The root of the smallest subtree containing all deepest nodes.
     */
    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        return getDeepestSubtree(root).node;
    }

    private NodeData getDeepestSubtree(TreeNode node) {
        if (node == null) {
            return new NodeData(null, 0);
        }

        NodeData left = getDeepestSubtree(node.left);
        NodeData right = getDeepestSubtree(node.right);

        if (left.depth == right.depth) {
            return new NodeData(node, left.depth + 1);
        } else if (left.depth > right.depth) {
            return new NodeData(left.node, left.depth + 1);
        } else {
            return new NodeData(right.node, right.depth + 1);
        }
    }
}