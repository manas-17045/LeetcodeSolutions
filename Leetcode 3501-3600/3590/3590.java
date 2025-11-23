// Leetcode 3590: Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/
// Solved on 23rd of November, 2025
import java.util.*;

class Solution {
    private List<Integer>[] adj;
    private List<int[]>[] nodeQueries;
    private int[] pathXor;
    private int[] sz;
    private int[] heavy;
    private int[] dfn;
    private int[] end;
    private int[] rank;
    private int timer;
    private int[] freq;
    private int[] bit;
    private int[] ans;
    private int maxVal = 131072;

    /**
     * Finds the k-th smallest XOR sum of paths from the root to specified nodes.
     * @param par An array representing the parent of each node. par[i] is the parent of node i. par[0] is -1 for the root.
     * @param vals An array where vals[i] is the value of node i.
     * @param queries A 2D array of queries, where each query[i] = [node, k] asks for the k-th smallest XOR sum from root to node.
     * @return An array of integers, where ans[i] is the answer to queries[i].
     */
    public int[] kthSmallest(int[] par, int[] vals, int[][] queries) {
        int n = par.length;
        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int i = 1; i < n; i++) {
            adj[par[i]].add(i);
        }

        pathXor = new int[n];
        sz = new int[n];
        heavy = new int[n];
        Arrays.fill(heavy, -1);
        dfn = new int[n];
        end = new int[n];
        rank = new int[n];
        timer = 0;

        nodeQueries = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            nodeQueries[i] = new ArrayList<>();
        }
        for (int i = 0; i < queries.length; i++) {
            nodeQueries[queries[i][0]].add(new int[]{queries[i][1], i});
        }

        dfsInit(0, 0, vals);

        freq = new int[maxVal + 2];
        bit = new int[maxVal + 2];
        ans = new int[queries.length];

        dfsSolve(0, true);
        return ans;
    }

    private void dfsInit(int u, int currentXor, int[] vals) {
        pathXor[u] = currentXor ^ vals[u];
        sz[u] = 1;
        dfn[u] = timer;
        rank[timer++] = u;
        int maxSz = -1;
        for (int v : adj[u]) {
            dfsInit(v, pathXor[u], vals);
            sz[u] += sz[v];
            if (sz[v] > maxSz) {
                maxSz = sz[v];
                heavy[u] = v;
            }
        }
        end[u] = timer - 1;
    }

    private void add(int val) {
        if (freq[val] == 0) {
            update(val + 1, 1);
        }
        freq[val]++;
    }

    private void remove(int val) {
        freq[val]--;
        if (freq[val] == 0) {
            update(val + 1, -1);
        }
    }

    private void update(int idx, int delta) {
        for (; idx <= maxVal + 1; idx += idx & -idx) {
            bit[idx] += delta;
        }
    }

    private int queryKth(int k) {
        int total = 0;
        for (int idx = maxVal + 1; idx > 0; idx -= idx & -idx) {
            total += bit[idx];
        }
        if (total < k) {
            return -1;
        }

        int idx = 0;
        int currentSum = 0;
        for (int i = 17; i >= 0; i--) {
            int nextIdx = idx + (1 << i);
            if (nextIdx <= maxVal + 1 && currentSum + bit[nextIdx] < k) {
                idx = nextIdx;
                currentSum += bit[idx];
            }
        }
        return idx;
    }

    private void dfsSolve(int u, boolean keep) {
        for (int v : adj[u]) {
            if (v != heavy[u]) {
                dfsSolve(v, false);
            }
        }
        if (heavy[u] != -1) {
            dfsSolve(heavy[u], true);
        }

        add(pathXor[u]);
        for (int v : adj[u]) {
            if (v != heavy[u]) {
                for (int i = dfn[v]; i <= end[v]; i++) {
                    add(pathXor[rank[i]]);
                }
            }
        }

        for (int[] q : nodeQueries[u]) {
            ans[q[1]] = queryKth(q[0]);
        }

        if (!keep) {
            for (int i = dfn[u]; i <= end[u]; i++) {
                remove(pathXor[rank[i]]);
            }
        }
    }
}