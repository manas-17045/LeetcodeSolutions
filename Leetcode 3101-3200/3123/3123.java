// Leetcode 3123: Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/
// Solved on 12th of December, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    /**
     * Finds all edges that are part of at least one shortest path from node 0 to node n-1.
     *
     * @param n The number of nodes in the graph.
     * @param edges A 2D array where each element `edges[i] = [u, v, w]` represents an undirected edge between nodes `u` and `v` with weight `w`.
     * @return A boolean array `result` of the same length as `edges`, where `result[i]` is `true` if `edges[i]` is part of a shortest path, and `false` otherwise.
     */
    public boolean[] findAnswer(int n, int[][]edges) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(new int[]{edge[1], edge[2]});
            graph.get(edge[1]).add(new int[]{edge[0], edge[2]});
        }

        long[] distFromStart = runDijkstra(n, graph, 0);
        long[] distFromEnd = runDijkstra(n, graph, n - 1);
        
        long shortestPath = distFromStart[n - 1];
        boolean[] result = new boolean[edges.length];
        
        if (shortestPath == Long.MAX_VALUE) {
            return result;
        }
        
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];
            
            long pathLen = Long.MAX_VALUE;
            
            if (distFromStart[u] != Long.MAX_VALUE && distFromEnd[v] != Long.MAX_VALUE) {
                pathLen = distFromStart[u] + w + distFromEnd[v];
            }
            
            if (pathLen != shortestPath) {
                if (distFromStart[v] != Long.MAX_VALUE && distFromEnd[u] != Long.MAX_VALUE) {
                    long reversePathLen = distFromStart[v] + w + distFromEnd[u];
                    if (reversePathLen == shortestPath) {
                        pathLen = reversePathLen;
                    }
                }
            }
            
            if (pathLen == shortestPath) {
                result[i] = true;
            }
        }
        
        return result;
    }

    private long[] runDijkstra(int n, List<List<int[]>> graph, int startNode) {
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[startNode] = 0;
        
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[1], b[1]));
        pq.offer(new long[]{startNode, 0});
        
        while (!pq.isEmpty()) {
            long[] current = pq.poll();
            int u = (int) current[0];
            long d = current[1];
            
            if (d > dist[u]) {
                continue;
            }
            
            for (int[] neighbor : graph.get(u)) {
                int v = neighbor[0];
                int w = neighbor[1];
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.offer(new long[]{v, dist[v]});
                }
            }
        }
        return dist;
    }
}