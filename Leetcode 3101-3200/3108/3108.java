// Leetcode 3108: Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
// Solved on 30th of October, 2025
class Solution {
    int[] parent;
    int[] size;
    int[] componentAnd;

    private int find(int i) {
        if (parent[i] == i) {
            return i;
        }
        parent[i] = find(parent[i]);
        return parent[i];
    }

    private void union(int u, int v, int w) {
        int rootU = find(u);
        int rootV = find(v);

        if (rootU != rootV) {
            if (size[rootU] < size[rootV]) {
                int temp = rootU;
                rootU = rootV;
                rootV = temp;
            }
            parent[rootV] = rootU;
            size[rootU] += size[rootV];
            componentAnd[rootU] = componentAnd[rootU] & componentAnd[rootV] & w;
        } else {
            componentAnd[rootU] = componentAnd[rootU] & w;
        }
    }

    /**
     * Calculates the minimum cost walk between two nodes in a weighted graph.
     * @param n The number of nodes in the graph.
     * @param edges A 2D array representing the edges of the graph, where each edge is [u, v, w].
     * @param query A 2D array representing the queries, where each query is [s, t].
     * @return An array of integers, where each element is the minimum cost for the corresponding query.
     */
    public int[] minimumCost(int n, int[][] edges, int[][] query) {
        parent = new int[n];
        size = new int[n];
        componentAnd = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
            componentAnd[i] = -1;
        }

        for (int[] edge : edges) {
            union(edge[0], edge[1], edge[2]);
        }

        int[] result = new int[query.length];
        for (int i = 0; i < query.length; i++) {
            int s = query[i][0];
            int t = query[i][1];

            int rootS = find(s);
            int rootT = find(t);

            if (rootS != rootT) {
                result[i] = -1;
            } else {
                result[i] = componentAnd[rootS];
            }
        }
        return result;
    }
}