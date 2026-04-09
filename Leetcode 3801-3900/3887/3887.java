// Leetcode 3887: Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/
// Solved on 9th of April, 2026
class Solution {
    /**
     * Calculates the number of edges that can be added while maintaining even-weighted cycles.
     * 
     * @param n The number of nodes in the graph.
     * @param edges A 2D array where each element is [u, v, w] representing an edge between u and v with weight w.
     * @return The total count of edges that satisfy the incremental cycle condition.
     */
    public int numberOfEdges(int n, int[][] edges) {
        int[] parent = new int[n];
        int[] weight = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
        int addedEdgesCount = 0;
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            int rootU = find(u, parent, weight);
            int rootV = find(v, parent, weight);
            if (rootU == rootV) {
                if ((weight[u] ^ weight[v]) == w) {
                    addedEdgesCount++;
                }
            } else {
                if (rank[rootU] > rank[rootV]) {
                    parent[rootV] = rootU;
                    weight[rootV] = weight[v] ^ weight[u] ^ w;
                } else if (rank[rootU] < rank[rootV]) {
                    parent[rootU] = rootV;
                    weight[rootU] = weight[u] ^ weight[v] ^ w;
                } else {
                    parent[rootU] = rootV;
                    weight[rootU] = weight[u] ^ weight[v] ^ w;
                    rank[rootV]++;
                }
                addedEdgesCount++;
            }
        }
        return addedEdgesCount;
    }

    private int find(int node, int[] parent, int[] weight) {
        if (parent[node] != node) {
            int oldParent = parent[node];
            parent[node] = find(parent[node], parent, weight);
            weight[node] ^= weight[oldParent];
        }
        return parent[node];
    }
}