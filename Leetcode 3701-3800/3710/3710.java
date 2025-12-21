// Leetcode 3710: Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/
// Solved on 21st of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Given an array of points, return the maximum partition factor.
     * The partition factor is defined as the maximum Manhattan distance D such that the points can be partitioned into two sets A and B,
     * where for any two points p1, p2 in the same set, their Manhattan distance is at most D, and for any two points p1 in A and p2 in B,
     * their Manhattan distance is greater than D.
     */
    public int maxPartitionFactor(int[][] points) {
        int n = points.length;
        if (n == 2) {
            return 0;
        }

        int edgeCount = n * (n - 1) / 2;
        long[] edges = new long[edgeCount];
        int idx = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long dist = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                edges[idx++] = (dist << 20) | (i << 10) | j;
            }
        }

        Arrays.sort(edges);

        int[] parent = new int[2 * n];
        for (int i = 0; i < 2 * n; i++) {
            parent[i] = i;
        }

        for (long edge : edges) {
            int dist = (int) (edge >>> 20);
            int u = (int) ((edge >>> 10) & 0x3FF);
            int v = (int) (edge & 0x3FF);

            int rootU = find(parent, u);
            int rootV = find(parent, v);

            if (rootU == rootV) {
                return dist;
            }

            union(parent, u, v + n);
            union(parent, v, u + n);
        }

        return 0;
    }

    private int find(int[] parent, int i) {
        if (parent[i] != i) {
            parent[i] = find(parent, parent[i]);
        }
        return parent[i];
    }

    private void union(int[] parent, int i, int j) {
        int rootI = find(parent, i);
        int rootJ = find(parent, j);
        if (rootI != rootJ) {
            parent[rootI] = rootJ;
        }
    }
}