// Leetcode 2830: Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/
// Solved on 4th of November, 2025
import java.util.*;

class Solution {
    /**
     * Maximizes the profit a salesman can make by selling gold in various plots.
     * @param n The number of plots available.
     * @param offers A list of offers, where each offer is [start_plot, end_plot, gold_amount].
     * @return The maximum profit that can be achieved.
     */
    public int maximizeTheProfit(int n, List<List<Integer>> offers) {

        List<int[]>[] starts = new ArrayList[n];

        for (int i = 0; i < n; i++) {
            starts[i] = new ArrayList<>();
        }

        for (List<Integer> offer : offers) {
            int s = offer.get(0);
            int e = offer.get(1);
            int g = offer.get(2);
            if (s >= 0 && s < n) {
                starts[s].add(new int[]{e, g});
            }
        }

        int[] dp = new int[n + 1];

        for (int i = n - 1; i >= 0; i--) {
            int best = dp[i + 1];
            for (int[] arr : starts[i]) {
                int end = arr[0];
                int gold = arr[1];
                int next = end + 1 <= n ? dp[end + 1] : 0;
                int cand = gold + next;
                if (cand > best) best = cand;
            }
            dp[i] = best;
        }

        return dp[0];
    }
}