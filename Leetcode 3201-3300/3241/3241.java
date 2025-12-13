// Leetcode 3241: Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/
// Solved on 13th of December, 2025
class Solution {
    private List<List<Integer>> adj;
    private int[] maxDist1;
    private int[] maxDist2;
    private int[] maxChild;
    private int[] result;

    /**
     * Calculates the time taken to mark all nodes in a tree, starting from each node.
     *
     * @param edges A 2D array representing the edges of the tree.
     * @return An array where result[i] is the minimum time to mark all nodes if node i is the starting node.
     */
    public int[] timeTaken(int[][] edges) {
        int n = edges.length + 1;
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        maxDist1 = new int[n];
        maxDist2 = new int[n];
        maxChild = new int[n];
        result = new int[n];

        dfsSubtree(0, -1);
        dfsSolve(0, -1, 0);

        return result;
    }

    private void dfsSubtree(int u, int p) {
        for (int v : adj.get(u)) {
            if (v == p) {
                continue;
            }
            dfsSubtree(v, u);

            int weight = (v % 2 != 0) ? 1 : 2;
            int dist = maxDist1[v] + weight;

            if (dist > maxDist1[u]) {
                maxDist2[u] = maxDist1[u];
                maxDist1[u] = dist;
                maxChild[u] = v;
            } else if (dist > maxDist2[u]) {
                maxDist2[u] = dist;
            }
        }
    }

    private void dfsSolve(int u, int p, int parentDist) {
        result[u] = Math.max(maxDist1[u], parentDist);

        for (int v : adj.get(u)) {
            if (v == p) {
                continue;
            }

            int maxFromU = (v == maxChild[u]) ? maxDist2[u] : maxDist1[u];
            int newParentDist = Math.max(parentDist, maxFromU);
            int weightToU = (u % 2 != 0) ? 1 : 2;

            dfsSolve(v, u, newParentDist + weightToU);
        }
    }
}