// Leetcode 3378: Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/
// Solved on 20th of November, 2025
class Solution {
    /**
     * Counts the number of connected components in an LCM graph.
     * @param nums An array of integers representing the nodes in the graph.
     * @param threshold The maximum value for which LCM connections are considered.
     * @return The total number of connected components.
     */
    public int countComponents(int[] nums, int threshold) {
        int[] parent = new int[threshold + 1];
        for (int i = 0; i <= threshold; i++) {
            parent[i] = i;
        }

        int componentCount = 0;
        for (int num : nums) {
            if (num > threshold) {
                componentCount++;
            } else {
                for (int multiple = 2 * num; multiple <= threshold; multiple += num) {
                    int rootA = find(parent, num);
                    int rootB = find(parent, multiple);
                    if (rootA != rootB) {
                        parent[rootA] = rootB;
                    }
                }
            }
        }

        boolean[] visited = new boolean[threshold + 1];
        for (int num : nums) {
            if (num <= threshold) {
                int root = find(parent, num);
                if (!visited[root]) {
                    visited[root] = true;
                    componentCount++;
                }
            }
        }

        return componentCount;
    }

    private int find(int[] parent, int node) {
        if (parent[node] == node) {
            return node;
        }
        return parent[node] = find(parent, parent[node]);
    }
}