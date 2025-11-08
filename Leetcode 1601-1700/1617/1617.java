// Leetcode 1617: Count Subtrees With Max Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-between-cities/
// Solved on 8th of November, 2025
import java.util.ArrayList;
import java.util.List;
import java.util.ArrayDeque;

class Solution {
    /**
     * Counts the number of subgraphs for each possible diameter.
     * @param n The number of cities.
     * @param edges A 2D array representing the connections between cities.
     * @return An array where `ans[d]` is the number of subgraphs with diameter `d + 1`.
     */
    public int[] countSubgraphsForEachDiameter(int n, int[][] edges) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] e : edges) {
            int u = e[0] - 1;
            int v = e[1] - 1;
            adj[u].add(v);
            adj[v].add(u);
        }
        int[] ans = new int[Math.max(0, n - 1)];
        int limit = 1 << n;
        for (int mask = 1; mask < limit; mask++) {
            int size = Integer.bitCount(mask);
            if (size < 2) {
                continue;
            }
            int edgeCount = 0;
            for (int[] e : edges) {
                int u = e[0] - 1;
                int v = e[1] - 1;
                if (((mask >> u) & 1) == 1 && ((mask >> v) & 1) == 1) {
                    edgeCount++;
                }
            }
            if (edgeCount != size - 1) {
                continue;
            }
            int start = -1;
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 1) {
                    start = i;
                    break;
                }
            }
            int farNode = bfsFarthest(start, mask, adj, n);
            int diameter = bfsDistance(farNode, mask, adj, n);
            if (diameter >= 1 && diameter <= n - 1) {
                ans[diameter - 1]++;
            }
        }
        return ans;
    }

    private int bfsFarthest(int src, int mask, List<Integer>[] adj, int n) {
        int[] dist = new int[n];
        for (int i = 0; i < n; i++) dist[i] = -1;
        ArrayDeque<Integer> q = new ArrayDeque<>();
        dist[src] = 0;
        q.add(src);
        int farNode = src;
        while (!q.isEmpty()) {
            int u = q.poll();
            if (dist[u] > dist[farNode]) farNode = u;
            for (int v : adj[u]) {
                if (((mask >> v) & 1) == 1 && dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.add(v);
                }
            }
        }
        return farNode;
    }

    private int bfsDistance(int src, int mask, List<Integer>[] adj, int n) {
        int[] dist = new int[n];
        for (int i = 0; i < n; i++) {
            dist[i] = -1;
        }
        ArrayDeque<Integer> q = new ArrayDeque<>();
        dist[src] = 0;
        q.add(src);
        int maxDist = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            if (dist[u] > maxDist) maxDist = dist[u];
            for (int v : adj[u]) {
                if (((mask >> v) & 1) == 1 && dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.add(v);
                }
            }
        }
        return maxDist;
    }
}