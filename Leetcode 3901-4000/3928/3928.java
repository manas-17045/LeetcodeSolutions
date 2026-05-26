// Leetcode 3928: Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/
// Solved on 26th of May, 2026
class Solution {

    private long[] heapData = new long[100000];
    private int heapSize = 0;

    private void push(long val) {
        heapData[++heapSize] = val;
        int i = heapSize;
        while (i > 1 && val < heapData[i >> 1]) {
            heapData[i] = heapData[i >> 1];
            i >>= 1;
        }
        heapData[i] = val;
    }

    private long pop() {
        long res = heapData[1];
        long val = heapData[heapSize--];
        if (heapSize == 0) {
            return res;
        }
        int i = 1;
        while ((i << 1) <= heapSize) {
            int child = i << 1;
            if (child < heapSize && heapData[child + 1] < heapData[child]) {
                child++;
            }
            if (val <= heapData[child]) {
                break;
            }
            heapData[i] = heapData[child];
            i = child;
        }
        heapData[i] = val;
        return res;
    }

    private void dijkstra(int start, int mode, long[] dist, int[] head, int[] to, int[] next, int[] weight, int[] taxArr) {
        for (int i = 0; i < dist.length; i++) {
            dist[i] = Long.MAX_VALUE;
        }
        dist[start] = 0;
        heapSize = 0;
        push((0L << 12) | start);

        while (heapSize > 0) {
            long curr = pop();
            long d = curr >>> 12;
            int u = (int) (curr & 0xFFF);

            if (d > dist[u]) {
                continue;
            }

            for (int e = head[u]; e != -1; e = next[e]) {
                int v = to[e];
                long w = mode == 0 ? weight[e] : (long) weight[e] * taxArr[e];
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    push((dist[v] << 12) | v);
                }
            }
        }
    }
    
    /**
     * Calculates the minimum cost to buy apples for each city.
     * 
     * @param n The number of cities.
     * @param prices An array where prices[i] is the cost of an apple in city i.
     * @param roads A 2D array representing roads between cities [u, v, weight, tax].
     * @return An array where the i-th element is the minimum cost to buy an apple starting from city i.
     */
    public int[] minCost(int n, int[] prices, int[][] roads) {
        int m = roads.length;
        int[] head = new int[n];
        for (int i = 0; i < n; i++) {
            head[i] = -1;
        }
        int[] to = new int[m * 2];
        int[] next = new int[m * 2];
        int[] weight = new int[m * 2];
        int[] taxArr = new int[m * 2];
        int edgeCount = 0;

        for (int i = 0; i < m; i++) {
            int u = roads[i][0];
            int v = roads[i][1];
            int w = roads[i][2];
            int t = roads[i][3];

            to[edgeCount] = v;
            weight[edgeCount] = w;
            taxArr[edgeCount] = t;
            next[edgeCount] = head[u];
            head[u] = edgeCount++;

            to[edgeCount] = u;
            weight[edgeCount] = w;
            taxArr[edgeCount] = t;
            next[edgeCount] = head[v];
            head[v] = edgeCount++;
        }

        long[] dist1 = new long[n];
        long[] dist2 = new long[n];
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            dijkstra(i, 0, dist1, head, to, next, weight, taxArr);
            dijkstra(i, 1, dist2, head, to, next, weight, taxArr);

            long minCost = Long.MAX_VALUE;
            for (int j = 0; j < n; j++) {
                if (dist1[j] != Long.MAX_VALUE && dist2[j] != Long.MAX_VALUE) {
                    long currentCost = dist1[j] + dist2[j] + prices[j];
                    if (currentCost < minCost) {
                        minCost = currentCost;
                    }
                }
            }
            ans[i] = (int) minCost;
        }

        return ans;
    }
}