// Leetcode 3650: Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/
// Solved on 28th of December, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class solution {
    /**
     * Calculates the minimum cost to travel from node 0 to node n-1 in a graph with edge reversals.
     * @param n The number of nodes in the graph.
     * @param edges A 2D array representing the edges, where each edge is [u, v, w] (from u to v with cost w).
     * @return The minimum cost to reach node n-1 from node 0, or -1 if unreachable.
     */
    public int minCost(int n, int[][] edges) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            graph.get(u).add(new int[]{v, w});
            graph.get(v).add(new int[]{u, 2 * w});
        }

        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, 0});

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int currentCost = current[0];
            int u = current[1];

            if (currentCost > dist[u]) {
                continue;
            }

            if (u == n - 1) {
                return currentCost;
            }

            for (int[] neighbor : graph.get(u)) {
                int v = neighbor[0];
                int weight = neighbor[1];
                int newCost = currentCost + weight;

                if (newCost < dist[v]) {
                    dist[v] = newCost;
                    pq.offer(new int[]{newCost, v});
                }
            }
        }

        return -1;
    }
}