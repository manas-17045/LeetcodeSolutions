// Leetcode 3559: Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/
// Solved on 12th of June, 2026
class Solution {
    int[] head;
    int[] to;
    int[] next;
    int edgeCount;
    int[] depth;
    int[][] up;

    /**
     * Calculates the number of ways to assign edge weights for given path queries in a tree.
     * @param edges A 2D array representing the edges of the tree.
     * @param queries A 2D array where each query is a pair of nodes [u, v].
     * @return An array of integers representing the number of ways for each query.
     */
    public int[] assignEdgeWeights(int[][] edges, int[][] queries) {
        int n = edges.length + 1;
        head = new int[n + 1];
        to = new int[n * 2];
        next = new int[n * 2];
        edgeCount = 1;
        
        for (int[] edge : edges) {
            addEdge(edge[0], edge[1]);
            addEdge(edge[1], edge[0]);
        }
        
        depth = new int[n + 1];
        up = new int[n + 1][18];
        
        dfs(1, 0, 0);
        
        for (int i = 1; i < 18; i++) {
            for (int j = 1; j <= n; j++) {
                up[j][i] = up[up[j][i - 1]][i - 1];
            }
        }
        
        int[] ans = new int[queries.length];
        int mod = 1000000007;
        
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            int lca = getLca(u, v);
            int pathLen = depth[u] + depth[v] - 2 * depth[lca];
            
            if (pathLen == 0) {
                ans[i] = 0;
            } else {
                ans[i] = power(2, pathLen - 1, mod);
            }
        }
        
        return ans;
    }

    void addEdge(int u, int v) {
        to[edgeCount] = v;
        next[edgeCount] = head[u];
        head[u] = edgeCount++;
    }

    void dfs(int node, int parent, int d) {
        depth[node] = d;
        up[node][0] = parent;
        for (int i = head[node]; i != 0; i = next[i]) {
            int neighbor = to[i];
            if (neighbor != parent) {
                dfs(neighbor, node, d + 1);
            }
        }
    }

    int getLca(int u, int v) {
        if (depth[u] < depth[v]) {
            int temp = u;
            u = v;
            v = temp;
        }
        for (int i = 17; i >= 0; i--) {
            if (depth[u] - (1 << i) >= depth[v]) {
                u = up[u][i];
            }
        }
        if (u == v) {
            return u;
        }
        for (int i = 17; i >= 0; i--) {
            if (up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }
        return up[u][0];
    }

    int power(long base, int exp, int mod) {
        long res = 1;
        base = base % mod;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * base) % mod;
            }
            exp >>= 1;
            base = (base * base) % mod;
        }
        return (int) res;
    }
}