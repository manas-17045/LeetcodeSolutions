// Leetcode 3772: Maximum Subgraph Score in a Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/
// Solved on 23rd of December, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer>[] adj;
    private int[] subtreeScore;
    private int[] result;
    private int[] nodeValues;

    /**
     * Calculates the maximum subgraph score for each node in a tree.
     * @param n The number of nodes in the tree.
     * @param edges A 2D array representing the edges of the tree.
     * @param good An array indicating whether each node is 'good' (1) or 'bad' (0).
     * @return An array where result[i] is the maximum subgraph score if node i is included.
     */
    public int[] maxSubgraphScore(int n, int[][] edges, int[] good) {
        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        
        for (int[] edge : edges) {
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }

        nodeValues = new int[n];
        for (int i = 0; i < n; i++) {
            nodeValues[i] = good[i] == 1 ? 1 : -1;
        }

        subtreeScore = new int[n];
        result = new int[n];

        dfsSubtree(0, -1);
        dfsReroot(0, -1);

        return result;
    }

    private void dfsSubtree(int u, int p) {
        subtreeScore[u] = nodeValues[u];
        for (int v : adj[u]) {
            if (v == p) {
                continue;
            }
            dfsSubtree(v, u);
            if (subtreeScore[v] > 0) {
                subtreeScore[u] += subtreeScore[v];
            }
        }
    }

    private void dfsReroot(int u, int p) {
        if (p == -1) {
            result[u] = subtreeScore[u];
        } else {
            int parentContribution = result[p];
            if (subtreeScore[u] > 0) {
                parentContribution -= subtreeScore[u];
            }

            result[u] = subtreeScore[u];
            if (parentContribution > 0) {
                result[u] += parentContribution;
            }
        }

        for (int v : adj[u]) {
            if (v == p) {
                continue;
            }
            dfsReroot(v, u);
        }
    }
}