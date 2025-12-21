// Leetcode 3715: Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/
// Solved on 21st of December, 2025
import java.util.Arrays;

class Solution {
    private int[] head;
    private int[] next;
    private int[] to;
    private int[] freq;
    private long total;
    private int[] values;

    /**
     * Calculates the sum of perfect square ancestors for each node in a tree.
     * @param n The number of nodes in the tree.
     * @param edges An array of edges representing the tree.
     * @param nums An array of values associated with each node.
     * @return The total sum of perfect square ancestors.
     */
    public long sumOfAncestors(int n, int[][] edges, int[] nums) {
        head = new int[n];
        Arrays.fill(head, -1);
        next = new int[2 * n];
        to = new int[2 * n];
        int idx = 0;

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            to[idx] = v;
            next[idx] = head[u];
            head[u] = idx++;
            to[idx] = u;
            next[idx] = head[v];
            head[v] = idx++;
        }

        freq = new int[100001];
        total = 0;
        values = nums;

        dfs(0, -1);

        return total;
    }

    private void dfs(int u, int p) {
        int val = values[u];
        int core = getSquareFreePart(val);

        total += freq[core];

        freq[core]++;

        for (int i = head[u]; i != -1; i = next[i]) {
            int v = to[i];
            if (v != p) {
                dfs(v, u);
            }
        }

        freq[core]--;
    }

    private int getSquareFreePart(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % (i * i) == 0) {
                while (n % (i * i) == 0) {
                    n /= (i * i);
                }
            }
        }
        return n;
    }
}