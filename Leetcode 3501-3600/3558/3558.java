// Leetcode 3558: Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/
// Solved on 22nd of October, 2025
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    /**
     * Calculates the number of ways to assign edge weights (0 or 1) to a tree such that the XOR sum
     * of weights along any path from the root (node 1) to any other node is 0.
     *
     * @param edges A 2D array where each inner array `[u, v]` represents an edge between node `u` and node `v`.
     * @return The number of ways to assign edge weights, modulo 1,000,000,007.
     */
    public int assignEdgeWeights(int[][] edges) {
        if (edges == null || edges.length == 0) return 0; // no valid input, but per constraints n>=2

        int n = edges.length + 1;
        ArrayList<Integer>[] adj = new ArrayList[n + 1];
        for (int i = 1; i <= n; ++i) adj[i] = new ArrayList<>();

        for (int[] e : edges) {
            int u = e[0], v = e[1];
            adj[u].add(v);
            adj[v].add(u);
        }

        // BFS from root 1 to compute maximum depth (distance in edges)
        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new ArrayDeque<>();
        dist[1] = 0;
        q.add(1);
        int maxDepth = 0;

        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    if (dist[v] > maxDepth) maxDepth = dist[v];
                    q.add(v);
                }
            }
        }

        // Answer = 2^(maxDepth - 1) mod MOD
        // Note: n >= 2 so maxDepth >= 1
        return (int) modPow(2, maxDepth - 1, MOD);
    }

    private long modPow(long base, long exp, int mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }
}