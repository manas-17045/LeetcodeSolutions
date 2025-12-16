// Leetcode 3510: Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/
// Solved on 16th of December, 2025
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the minimum number of pair removals to sort the array.
     *
     * @param nums The input array of integers.
     * @return The minimum number of operations required.
     */
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        if (n <= 1) {
            return 0;
        }

        long[] val = new long[n];
        int[] next = new int[n];
        int[] prev = new int[n];
        boolean[] removed = new boolean[n];

        for (int i = 0; i < n; i++) {
            val[i] = nums[i];
            next[i] = (i == n - 1) ? -1 : i + 1;
            prev[i] = (i == 0) ? -1 : i - 1;
        }

        int badCount = 0;
        for (int i = 0; i < n - 1; i++) {
            if (val[i] > val[i + 1]) {
                badCount++;
            }
        }

        if (badCount == 0) {
            return 0;
        }

        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> {
            int cmp = Long.compare(a[0], b[0]);
            if (cmp != 0) {
                return cmp;
            }
            return Long.compare(a[1], b[1]);
        });

        for (int i = 0; i < n - 1; i++) {
            pq.offer(new long[]{val[i] + val[i + 1], i, i + 1});
        }

        int ops = 0;

        while (badCount > 0 && !pq.isEmpty()) {
            long[] top = pq.poll();
            long sum = top[0];
            int u = (int) top[1];
            int v = (int) top[2];

            if (removed[u] || next[u] != v || val[u] + val[v] != sum) {
                continue;
            }

            ops++;
            int h = prev[u];
            int w = next[v];

            if (val[u] > val[v]) {
                badCount--;
            }
            if (h != -1 && val[h] > val[u]) {
                badCount--;
            }
            if (w != -1 && val[v] > val[w]) {
                badCount--;
            }

            val[u] += val[v];
            removed[v] = true;
            next[u] = w;
            if (w != -1) {
                prev[w] = u;
            }

            if (h != -1) {
                if (val[h] > val[u]) {
                    badCount++;
                }
                pq.offer(new long[]{val[h] + val[u], h, u});
            }
            if (w != -1) {
                if (val[u] > val[w]) {
                    badCount++;
                }
                pq.offer(new long[]{val[u] + val[w], u, w});
            }
        }

        return ops;
    }
}