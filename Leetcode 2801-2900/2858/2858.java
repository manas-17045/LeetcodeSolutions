// Leetcode 2858: Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/
// Solved on 7th of March, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    List<List<int[]>> graph;
    int[] result;

    /**
     * Calculates the minimum number of edge reversals required for each node to be able to reach all other nodes.
     *
     * @param n     The number of nodes in the graph.
     * @param edges A 2D array representing directed edges where edges[i] = [ui, vi].
     * @return      An array where the i-th element is the minimum reversals needed if node i is the root.
     */
    public int[] minEdgeReversals(int n, int[][] edges) {
        graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            graph.get(u).add(new int[]{v, 0});
            graph.get(v).add(new int[]{u, 1});
        }
        
        result = new int[n];
        result[0] = dfsOne(0, -1);
        dfsTwo(0, -1);
        
        return result;
    }

    private int dfsOne(int current, int parent) {
        int cost = 0;
        for (int[] neighbor : graph.get(current)) {
            int next = neighbor[0];
            int weight = neighbor[1];
            if (next != parent) {
                cost += weight + dfsOne(next, current);
            }
        }
        return cost;
    }

    private void dfsTwo(int current, int parent) {
        for (int[] neighbor : graph.get(current)) {
            int next = neighbor[0];
            int weight = neighbor[1];
            if (next != parent) {
                result[next] = result[current] + (weight == 1 ? -1 : 1);
                dfsTwo(next, current);
            }
        }
    }
}