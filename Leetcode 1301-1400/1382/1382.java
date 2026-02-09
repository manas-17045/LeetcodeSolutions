// Leetcode 1328: Balance a Binary Search Tree
// https://leetcode.com/problems/balance-a-binary-search-tree/
// Solved on 9th of February, 2026
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
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Balances a binary search tree so that the depth of the two subtrees of every node never differs by more than one.
     * @param root The root of the original binary search tree.
     * @return The root of the newly balanced binary search tree.
     */
    public TreeNode balanceBST(TreeNode root) {
        List<TreeNode> sortedNodes = new ArrayList<>();
        inorderTraversal(root, sortedNodes);
        return constructBalancedTree(sortedNodes, 0, sortedNodes.size() - 1);
    }

    private void inorderTraversal(TreeNode node, List<TreeNode> sortedNodes) {
        if (node == null) {
            return;
        }
        inorderTraversal(node.left, sortedNodes);
        sortedNodes.add(node);
        inorderTraversal(node.right, sortedNodes);
    }

    private TreeNode constructBalancedTree(List<TreeNode> sortedNodes, int start, int end) {
        if (start > end) {
            return null;
        }
        int mid = start + (end - start) / 2;
        TreeNode node = sortedNodes.get(mid);
        node.left = constructBalancedTree(sortedNodes, start, mid - 1);
        node.right = constructBalancedTree(sortedNodes, mid + 1, end);
        return node;
    }
}