// Leetcode 1361: Validate Binary Tree Nodes
// https://leetcode.com/problems/validate-binary-tree-nodes/
// Solved on 8th of March, 2026
class Solution {
    /**
     * Validates if the given nodes form exactly one valid binary tree.
     * 
     * @param n The number of nodes indexed from 0 to n - 1.
     * @param leftChild The left child of each node i, or -1 if none.
     * @param rightChild The right child of each node i, or -1 if none.
     * @return True if the nodes form a single valid binary tree, false otherwise.
     */
    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        int[] inDegree = new int[n];
        for (int i = 0; i < n; i++) {
            if (leftChild[i] != -1) {
                inDegree[leftChild[i]]++;
                if (inDegree[leftChild[i]] > 1) {
                    return false;
                }
            }
            if (rightChild[i] != -1) {
                inDegree[rightChild[i]]++;
                if (inDegree[rightChild[i]] > 1) {
                    return false;
                }
            }
        }
        int root = -1;
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                if (root != -1) {
                    return false;
                }
                root = i;
            }
        }
        if (root == -1) {
            return false;
        }
        int[] queue = new int[n];
        int head = 0;
        int tail = 0;
        queue[tail++] = root;
        int count = 0;
        while (head < tail) {
            int curr = queue[head++];
            count++;
            if (leftChild[curr] != -1) {
                queue[tail++] = leftChild[curr];
            }
            if (rightChild[curr] != -1) {
                queue[tail++] = rightChild[curr];
            }
        }
        return count == n;
    }
}