// Leetcode 3532: Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/
// Solved on 29th of October, 2025
class Solution {
    
    private int find(int[] parent, int i) {
        if (parent[i] == i) {
            return i;
        }
        parent[i] = find(parent, parent[i]);
        return parent[i];
    }

    private void union(int[] parent, int[] size, int i, int j) {
        int rootI = find(parent, i);
        int rootJ = find(parent, j);
        if (rootI != rootJ) {
            if (size[rootI] < size[rootJ]) {
                parent[rootI] = rootJ;
                size[rootJ] += size[rootI];
            } else {
                parent[rootJ] = rootI;
                size[rootI] += size[rootJ];
            }
        }
    }

    /**
     * Determines if a path exists between two nodes in a graph based on a maximum difference constraint.
     * @param n The number of nodes in the graph.
     * @param nums An array representing values associated with each node.
     * @param maxDiff The maximum allowed difference between values of adjacent nodes for a path to exist.
     * @param queries A 2D array of queries, where each query `[u, v]` asks if a path exists between node `u` and node `v`.
     * @return A boolean array where `answer[k]` is true if a path exists for `queries[k]`, and false otherwise.
     */
    public boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] parent = new int[n];
        int[] size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        
        for (int i = 1; i < n; i++) {
            if (nums[i] - nums[i - 1] <= maxDiff) {
                union(parent, size, i, i - 1);
            }
        }
        
        int numQueries = queries.length;
        boolean[] answer = new boolean[numQueries];
        for (int k = 0; k < numQueries; k++) {
            int u = queries[k][0];
            int v = queries[k][1];
            answer[k] = (find(parent, u) == find(parent, v));
        }
        
        return answer;
    }
}