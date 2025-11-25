// Leetcode 3620: Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/
// Solved on 25th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Finds the maximum possible path score from node 0 to node n-1 such that the total path weight is at most `k`.
     * The path score is defined as the minimum edge weight along the path.
     * Nodes other than the start (0) and end (n-1) must be "online" to be part of the path.
     *
     * @param edges A 2D array where each inner array `[u, v, w]` represents a directed edge from `u` to `v` with weight `w`.
     * @param online A boolean array where `online[i]` is true if node `i` is online, and false otherwise.
     * @param k The maximum allowed total path weight.
     * @return The maximum path score, or -1 if no such path exists.
     */
    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {
        int n = online.length;
        int m = edges.length;
        int[] head = new int[n];
        Arrays.fill(head, -1);
        int[] next = new int[m];
        int[] to = new int[m];
        int[] weight = new int[m];
        int[] inDegree = new int[n];

        for (int i = 0; i < m; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];
            to[i] = v;
            weight[i] = w;
            next[i] = head[u];
            head[u] = i;
            inDegree[v]++;
        }

        int[] topo = new int[n];
        int tail = 0;
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                topo[tail++] = i;
            }
        }

        int headIdx = 0;
        while (headIdx < tail) {
            int u = topo[headIdx++];
            for (int e = head[u]; e != -1; e = next[e]) {
                int v = to[e];
                inDegree[v]--;
                if (inDegree[v] == 0) {
                    topo[tail++] = v;
                }
            }
        }

        int low = 0;
        int high = 1000000000;
        int ans = -1;
        long[] dist = new long[n];

        while (low <= high) {
            int mid = low + (high - low) / 2;
            Arrays.fill(dist, -1);
            dist[0] = 0;

            for (int i = 0; i < n; i++) {
                int u = topo[i];
                if (dist[u] == -1) {
                    continue;
                }

                for (int e = head[u]; e != -1; e = next[e]) {
                    int v = to[e];
                    int w = weight[e];

                    if (w < mid) {
                        continue;
                    }
                    if (v != n - 1 && !online[v]) {
                        continue;
                    }

                    if (dist[v] == -1 || dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                    }
                }
            }

            if (dist[n - 1] != -1 && dist[n - 1] <= k) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans;
    }
}