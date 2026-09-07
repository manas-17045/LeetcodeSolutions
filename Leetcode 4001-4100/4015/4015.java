// Leetcode 4015: Weighted Sum of a Tree
// https://leetcode.com/problems/weighted-sum-of-a-tree/
// Solved on 7th of September, 2026
class Solution {
    /**
     * Calculates the weighted sum of all nodes in a rooted tree, where each
     * node's weight is determined by its value and its distance from the maximum depth.
     *
     * @param parent an array where parent[i] indicates the parent node of node i
     * @param nums an array where nums[i] represents the value assigned to node i
     * @return the total weighted sum of all nodes in the tree
     */
    public long weightedSum(int[] parent, int[] nums) {
        int n = parent.length;
        int[] depth = new int[n];
        depth[0] = 1;
        int maxHeight = 1;

        for (int i = 1; i < n; i++) {
            if (depth[i] != 0) {
                continue;
            }

            int curr = i;
            int steps = 0;
            while (depth[curr] == 0) {
                steps++;
                curr = parent[curr];
            }

            int knownDepth = depth[curr];
            curr = i;
            while (depth[curr] == 0) {
                int nodeDepth = knownDepth + steps;
                depth[curr] = nodeDepth;
                if (nodeDepth > maxHeight) {
                    maxHeight = nodeDepth;
                }
                steps--;
                curr = parent[curr];
            }
        }

        long totalSum = 0;
        for (int i = 0; i < n; i++) {
            totalSum += (long) nums[i] * (maxHeight - depth[i] + 1);
        }

        return totalSum;
    }
}