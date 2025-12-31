// Leetcode 3419: Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/
// Solved on 31st of December, 2025
import java.util.*;

class Solution {
    /**
     * Minimizes the maximum edge weight of a graph such that all nodes are reachable from node 0.
     * @param n The number of nodes in the graph.
     * @param edges A 2D array representing the edges, where `edges[i] = [u, v, w]` means an edge from `u` to `v` with weight `w`.
     * @param threshold This parameter is not used in the current implementation.
     * @return The minimum possible value for the maximum edge weight that allows all nodes to be reachable from node 0.
     */
    public int minMaxWeight(int n, int[][] edges, int threshold) {
        List<int[]>[] reversedGraph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            reversedGraph[i] = new ArrayList<>();
        }

        int minWeight = Integer.MAX_VALUE;
        int maxWeight = Integer.MIN_VALUE;

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            reversedGraph[v].add(new int[]{u, w});
            minWeight = Math.min(minWeight, w);
            maxWeight = Math.max(maxWeight, w);
        }

        int left = minWeight;
        int right = maxWeight;
        int result = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canReachAll(n, reversedGraph, mid)) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return result;
    }

    private boolean canReachAll(int n, List<int[]>[] graph, int maxW) {
        int count = 0;
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new ArrayDeque<>();

        queue.offer(0);
        visited[0] = true;
        count++;

        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int[] edge : graph[u]) {
                int v = edge[0];
                int w = edge[1];
                if (w <= maxW && !visited[v]) {
                    visited[v] = true;
                    count++;
                    queue.offer(v);
                }
            }
        }

        return count == n;
    }
}