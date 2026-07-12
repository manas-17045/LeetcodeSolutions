// Leetcode 3970: Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/
// Solved on 12th of July, 2026
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    /**
     * Finds the shortest path from node 0 to node n-1 with at most k consecutive identical characters.
     * 
     * @param n      The number of nodes.
     * @param edges  The edges.
     * @param labels The labels.
     * @param k      The maximum number of consecutive identical characters.
     * @return The shortest path.
     */
    public int shortestPath(int n, int[][] edges, String labels, int k) {
        int edgeCount = edges.length;
        int[] head = new int[n];
        int[] to = new int[edgeCount];
        int[] weight = new int[edgeCount];
        int[] next = new int[edgeCount];
        java.util.Arrays.fill(head, -1);
        for (int i = 0; i < edgeCount; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];
            to[i] = v;
            weight[i] = w;
            next[i] = head[u];
            head[u] = i;
        }
        int[][] dist = new int[n][k + 1];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }
        dist[0][1] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        pq.offer(new int[]{0, 0, 1});
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int d = curr[0];
            int u = curr[1];
            int count = curr[2];
            if (u == n - 1) {
                return d;
            }
            if (d > dist[u][count]) {
                continue;
            }
            char currChar = labels.charAt(u);
            for (int e = head[u]; e != -1; e = next[e]) {
                int v = to[e];
                int w = weight[e];
                char nextChar = labels.charAt(v);
                int nextCount = (currChar == nextChar) ? count + 1 : 1;
                if (nextCount <= k && d + w < dist[v][nextCount]) {
                    dist[v][nextCount] = d + w;
                    pq.offer(new int[]{d + w, v, nextCount});
                }
            }
        }
        return -1;
    }
}