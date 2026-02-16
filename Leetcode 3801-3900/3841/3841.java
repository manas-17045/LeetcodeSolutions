// Leetcode 3841: Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/
// Solved on 16th of February, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    List<Integer>[] adj;
    int[] inTime;
    int[] outTime;
    int[][] up;
    int timer;
    int[] fenwick;
    int[] nodeValues;
    int n;

    /**
     * Processes queries on a tree to determine if the path between two nodes can form a palindrome.
     * Supports point updates on node characters.
     *
     * @param n The number of nodes in the tree.
     * @param edges A 2D array representing the edges of the tree.
     * @param s A string where s[i] is the character assigned to node i.
     * @param queries A list of strings representing "update u char" or "query u v" operations.
     * @return A list of booleans indicating if the path for each query can form a palindrome.
     */
    public List<Boolean> palindromePath(int n, int[][] edges, String s, String queries) {
        this.n = n;
        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }

        inTime = new int[n];
        outTime = new int[n];
        up = new int[n][17];
        timer = 0;

        dfs(0, 0);

        fenwick = new int[n + 2];
        nodeValues = new int[n];

        for (int i = 0; i < n; i++) {
            int val = 1 << (s.charAt(i) - 'a');
            nodeValues[i] = val;
            updateFenwick(inTime[i], val);
            updateFenwick(outTime[i] + 1, val);
        }

        List<Boolean> result = new ArrayList<>();
        for (String q : queries) {
            String[] parts = q.split(" ");
            if (parts[0].equals("update")) {
                int u = Integer.parseInt(parts[1]);
                int newVal = 1 << (parts[2].charAt(0) - 'a');
                int diff = nodeValues[u] ^ newVal;
                nodeValues[u] = newVal;
                updateFenwick(inTime[u], diff);
                updateFenwick(outTime[u] + 1, diff);
            } else {
                int u = Integer.parseInt(parts[1]);
                int v = Integer.parseInt(parts[2]);
                int maskU = queryFenwick(inTime[u]);
                int maskV = queryFenwick(inTime[v]);
                int lca = getLca(u, v);
                int pathMask = maskU ^ maskV ^ nodeValues[lca];
                result.add(Integer.bitCount(pathMask) <= 1);
            }
        }
        return result;
    }

    private void dfs(int u, int p) {
        inTime[u] = ++timer;
        up[u][0] = p;
        for (int i = 1; i < 17; i++) {
            up[u][i] = up[up[u][i - 1]][i - 1];
        }
        for (int v : adj[u]) {
            if (v != p) {
                dfs(v, u);
            }
        }
        outTime[u] = timer;
    }

    private boolean isAncestor(int u, int v) {
        return inTime[u] <= inTime[v] && outTime[u] >= outTime[v];
    }

    private int getLca(int u, int v) {
        if (isAncestor(u, v)) {
            return u;
        }
        if (isAncestor(v, u)) {
            return v;
        }
        for (int i = 16; i >= 0; i--) {
            if (!isAncestor(up[u][i], v)) {
                u = up[u][i];
            }
        }
        return up[u][0];
    }

    private void updateFenwick(int idx, int val) {
        while (idx <= n + 1) {
            fenwick[idx] ^= val;
            idx += idx & -idx;
        }
    }

    private int queryFenwick(int idx) {
        int res = 0;
        while (idx > 0) {
            res ^= fenwick[idx];
            idx -= idx & -idx;
        }
        return res;
    }
}