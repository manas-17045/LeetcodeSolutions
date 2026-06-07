// Leetcode 2196: Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/
// Solved on 7th of June, 2026
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) {
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    /**
     * Creates a binary tree from a 2D array of descriptions.
     * 
     * @param descriptions An array where descriptions[i] = [parent, child, isLeft]
     * @return The root of the constructed binary tree.
     */
    public TreeNode createBinaryTree(int[][] descriptions) {
        TreeNode[] nodeMap = new TreeNode[100001];
        boolean[] isChild = new boolean[100001];

        for (int[] desc : descriptions) {
            int parentVal = desc[0];
            int childVal = desc[1];
            int isLeft = desc[2];

            if (nodeMap[parentVal] == null) {
                nodeMap[parentVal] = new TreeNode(parentVal);
            }
            if (nodeMap[childVal] == null) {
                nodeMap[childVal] = new TreeNode(childVal);
            }

            if (isLeft == 1) {
                nodeMap[parentVal].left = nodeMap[childVal];
            } else {
                nodeMap[parentVal].right = nodeMap[childVal];
            }

            isChild[childVal] = true;
        }

        for (int[] desc : descriptions) {
            int parentVal = desc[0];
            if (!isChild[parentVal]) {
                return nodeMap[parentVal];
            }
        }

        return null;
    }
}