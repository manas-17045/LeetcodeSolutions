// Leetcode 3613: Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/
// Solved on 25th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Minimizes the maximum cost of a component such that there are at most `k` components.
     * This is achieved by using a Kruskal-like algorithm.
     * @param n The number of nodes in the graph.
     * @param edges A 2D array where each inner array `[u, v, cost]` represents an edge between nodes `u` and `v` with a given `cost`.
     * @param k The maximum allowed number of components.
     * @return The minimum possible maximum cost of an edge in any component such that the number of components is at most `k`.
     */
    public int minCost(int n, int[][] edges, int k) {
        if (n <= k) {
            return 0;
        }
        Arrays.sort(edges, (a, b) -> Integer.compare(a[2], b[2]));
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        int components = n;
        for (int[] edge : edges) {
            int rootU = find(parent, edge[0]);
            int rootV = find(parent, edge[1]);
            if (rootU != rootV) {
                parent[rootU] = rootV;
                components--;
            }
            if (components <= k) {
                return edge[2];
            }
        }
        return 0;
    }

    private int find(int[] parent, int i) {
        while (i != parent[i]) {
            parent[i] = parent[parent[i]];
            i = parent[i];
        }
        return i;
    }
}