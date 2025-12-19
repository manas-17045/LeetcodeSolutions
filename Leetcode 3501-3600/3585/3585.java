// Leetcode 3585: Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/
// Solved on 19th of December, 2025
import java.util.*;

class Solution {
    private List<int[]>[] adj;
    private int[][] up;
    private int[] depth;
    private long[] dist;
    private int LOG;

    /**
     * Finds the weighted median node for a set of queries in a tree.
     *
     * @param n The number of nodes in the tree.
     * @param edges A 2D array representing the edges of the tree, where edges[i] = [u, v, w] means an edge between u and v with weight w.
     * @param queries A 2D array of queries, where queries[i] = [u, v] represents a query for the weighted median node on the path between u and v.
     * @return An array of integers, where ans[i] is the weighted median node for queries[i].
     */
    public int[] findMedian(int n, int[][] edges, int[][] queries) {
        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] e : edges) {
            adj[e[0]].add(new int[]{e[1], e[2]});
            adj[e[1]].add(new int[]{e[0], e[2]});
        }

        LOG = Integer.numberOfTrailingZeros(Integer.highestOneBit(n)) + 1;
        up = new int[n][LOG + 1];
        depth = new int[n];
        dist = new long[n];

        dfs(0, -1, 0, 0);

        for (int j = 1; j <= LOG; j++) {
            for (int i = 0; i < n; i++) {
                if (up[i][j - 1] != -1) {
                    up[i][j] = up[up[i][j - 1]][j - 1];
                } else {
                    up[i][j] = -1;
                }
            }
        }

        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            ans[i] = solve(queries[i][0], queries[i][1]);
        }
        return ans;
    }

    private void dfs(int u, int p, int d, long w) {
        depth[u] = d;
        dist[u] = w;
        up[u][0] = p;
        for (int[] e : adj[u]) {
            if (e[0] != p) {
                dfs(e[0], u, d + 1, w + e[1]);
            }
        }
    }

    private int getLca(int u, int v) {
        if (depth[u] < depth[v]) {
            int temp = u; u = v; v = temp;
        }
        for (int j = LOG; j >= 0; j--) {
            if (up[u][j] != -1 && depth[up[u][j]] >= depth[v]) {
                u = up[u][j];
            }
        }
        if (u == v) return u;
        for (int j = LOG; j >= 0; j--) {
            if (up[u][j] != up[v][j]) {
                u = up[u][j];
                v = up[v][j];
            }
        }
        return up[u][0];
    }

    private int solve(int u, int v) {
        int lca = getLca(u, v);
        long pathWeight = dist[u] + dist[v] - 2 * dist[lca];

        long distUtoLca = dist[u] - dist[lca];

        if (2 * distUtoLca >= pathWeight) {
            if (0 >= pathWeight) {
                return u;
            }

            int curr = u;
            for (int j = LOG; j >= 0; j--) {
                int next = up[curr][j];
                if (next != -1 && depth[next] >= depth[lca]) {
                    long d = dist[u] - dist[next];
                    if (2 * d < pathWeight) {
                        curr = next;
                    }
                }
            }
            return up[curr][0];
        } else {
            long rhs = pathWeight - 2 * dist[u] + 4 * dist[lca];
            int curr = v;

            for (int j = LOG; j >= 0; j--) {
                int next = up[curr][j];
                if (next != -1 && depth[next] > depth[lca]) {
                    if (2 * dist[next] >= rhs) {
                        curr = next;
                    }
                }
            }
            return curr;
        }
    }
}