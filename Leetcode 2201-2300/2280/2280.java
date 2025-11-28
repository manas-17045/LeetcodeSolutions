// Leetcode 2280: Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/
// Solved on 28th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum number of lines required to represent a line chart given stock prices.
     * A new line is needed if three consecutive points are not collinear.
     * @param stockPrices A 2D array where stockPrices[i] = [day_i, price_i].
     * @return The minimum number of lines.
     */
    public int minimumLines(int[][] stockPrices) {
        if (stockPrices.length == 1) {
            return 0;
        }

        Arrays.sort(stockPrices, (a, b) -> a[0] - b[0]);

        int count = 1;

        for (int i = 2; i < stockPrices.length; i++) {
            long x1 = stockPrices[i - 2][0];
            long y1 = stockPrices[i - 2][1];
            long x2 = stockPrices[i - 1][0];
            long y2 = stockPrices[i - 1][1];
            long x3 = stockPrices[i][0];
            long y3 = stockPrices[i][1];

            long diffY1 = y2 - y1;
            long diffX1 = x2 - x1;
            long diffY2 = y3 - y2;
            long diffX2 = x3 - x2;

            if (diffY1 * diffX2 != diffY2 * diffX1) {
                count++;
            }
        }

        return count;
    }
}