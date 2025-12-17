// Leetcode 3553: Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/
// Solved on 17th of December, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private List<int[]>[] adj;
    private int[][] up;
    private int[] depth;
    private int[] level;
    private int log;

    /**
     * Calculates the minimum weighted subgraph with the required paths for multiple queries.
     *
     * @param edges A 2D array representing the edges of the graph. Each edge is [u, v, weight].
     * @param queries A 2D array representing the queries. Each query is [src1, src2, dest].
     * @return An array of integers, where each element is the minimum total weight for the corresponding query.
     *         The total weight is the sum of distances from src1 to median, src2 to median, and dest to median,
     *         where median is the "center" of the three nodes (src1, src2, dest).
     */
    public int[] minimumWeight(int[][] edges, int[][] queries) {
        int n = edges.length + 1;
        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            adj[edge[0]].add(new int[]{edge[1], edge[2]});
            adj[edge[1]].add(new int[]{edge[0], edge[2]});
        }

        log = 0;
        while ((1 << log) <= n) {
            log++;
        }

        up = new int[n][log];
        depth = new int[n];
        level = new int[n];
        
        bfs(0, n);

        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int src1 = queries[i][0];
            int src2 = queries[i][1];
            int dest = queries[i][2];

            int lca1 = getLca(src1, src2);
            int lca2 = getLca(src1, dest);
            int lca3 = getLca(src2, dest);

            int median = lca1;
            if (level[lca2] > level[median]) {
                median = lca2;
            }
            if (level[lca3] > level[median]) {
                median = lca3;
            }

            long dist1 = getDist(src1, median);
            long dist2 = getDist(src2, median);
            long dist3 = getDist(dest, median);

            answer[i] = (int) (dist1 + dist2 + dist3);
        }

        return answer;
    }

    private void bfs(int start, int n) {
        boolean[] visited = new boolean[n];
        int[] q = new int[n];
        int head = 0, tail = 0;
        
        q[tail++] = start;
        visited[start] = true;
        level[start] = 0;
        depth[start] = 0;

        while (head < tail) {
            int u = q[head++];
            
            for (int i = 1; i < log; i++) {
                up[u][i] = up[up[u][i - 1]][i - 1];
            }

            for (int[] next : adj[u]) {
                int v = next[0];
                int weight = next[1];
                if (!visited[v]) {
                    visited[v] = true;
                    level[v] = level[u] + 1;
                    depth[v] = depth[u] + weight;
                    up[v][0] = u;
                    q[tail++] = v;
                }
            }
        }
    }

    private int getLca(int u, int v) {
        if (level[u] < level[v]) {
            int temp = u;
            u = v;
            v = temp;
        }

        for (int i = log - 1; i >= 0; i--) {
            if (level[u] - (1 << i) >= level[v]) {
                u = up[u][i];
            }
        }

        if (u == v) {
            return u;
        }

        for (int i = log - 1; i >= 0; i--) {
            if (up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }

        return up[u][0];
    }

    private long getDist(int u, int v) {
        return (long) depth[u] + depth[v] - 2L * depth[getLca(u, v)];
    }
}