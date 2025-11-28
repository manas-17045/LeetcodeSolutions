// Leetcode 3562: Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/
// Solved on 28th of November, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private List<List<Integer>> tree;
    private int[] currentPrices;
    private int[] futurePrices;
    private int maxBudget;

    /**
     * Calculates the maximum profit from trading stocks with discounts.
     *
     * @param n The number of stocks.
     * @param present An array where present[i] is the current price of the i-th stock.
     * @param future An array where future[i] is the future price of the i-th stock.
     * @param hierarchy A 2D array representing the hierarchy of stocks, where hierarchy[j] = [u, v] means stock u is the parent of stock v.
     * @param budget The maximum budget available.
     * @return The maximum profit that can be achieved.
     */
    public int maxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        this.currentPrices = present;
        this.futurePrices = future;
        this.maxBudget = budget;
        this.tree = new ArrayList<>();

        for (int i = 0; i <= n; i++) {
            tree.add(new ArrayList<>());
        }

        for (int[] relation : hierarchy) {
            tree.get(relation[0]).add(relation[1]);
        }

        int[][] result = dfs(1);

        int maxProfit = 0;
        for (int value : result[0]) {
            maxProfit = Math.max(maxProfit, value);
        }

        return maxProfit;
    }

    private int[][] dfs(int u) {
        int[][] res = new int[2][maxBudget + 1];
        int minVal = -1000000000;
        Arrays.fill(res[0], minVal);
        Arrays.fill(res[1], minVal);

        int[] dpNoBuy = new int[maxBudget + 1];
        int[] dpBuy = new int[maxBudget + 1];
        Arrays.fill(dpNoBuy, minVal);
        Arrays.fill(dpBuy, minVal);
        dpNoBuy[0] = 0;
        dpBuy[0] = 0;

        for (int v : tree.get(u)) {
            int[][] childRes = dfs(v);
            dpNoBuy = merge(dpNoBuy, childRes[0], minVal);
            dpBuy = merge(dpBuy, childRes[1], minVal);
        }

        int price = currentPrices[u - 1];
        int profit = futurePrices[u - 1] - price;

        for (int b = 0; b <= maxBudget; b++) {
            if (dpNoBuy[b] != minVal) {
                res[0][b] = Math.max(res[0][b], dpNoBuy[b]);
            }
            if (b >= price && dpBuy[b - price] != minVal) {
                res[0][b] = Math.max(res[0][b], dpBuy[b - price] + profit);
            }
        }

        int halfPrice = price / 2;
        int halfProfit = futurePrices[u - 1] - halfPrice;

        for (int b = 0; b <= maxBudget; b++) {
            if (dpNoBuy[b] != minVal) {
                res[1][b] = Math.max(res[1][b], dpNoBuy[b]);
            }
            if (b >= halfPrice && dpBuy[b - halfPrice] != minVal) {
                res[1][b] = Math.max(res[1][b], dpBuy[b - halfPrice] + halfProfit);
            }
        }

        return res;
    }

    private int[] merge(int[] dp, int[] childDp, int minVal) {
        int[] nextDp = new int[maxBudget + 1];
        Arrays.fill(nextDp, minVal);

        for (int b = maxBudget; b >= 0; b--) {
            for (int k = 0; k <= b; k++) {
                if (dp[b - k] != minVal && childDp[k] != minVal) {
                    nextDp[b] = Math.max(nextDp[b], dp[b - k] + childDp[k]);
                }
            }
        }
        return nextDp;
    }
}