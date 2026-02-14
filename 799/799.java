// Leetcode 799: Champagne Tower
// https://leetcode.com/problems/champagne-tower/
// Solved on 14th of February, 2026
class Solution {
    /**
     * Simulates the flow of champagne through a tower of glasses.
     *
     * @param poured      The total number of units of champagne poured into the top glass.
     * @param query_row   The 0-indexed row of the glass to query.
     * @param query_glass The 0-indexed index of the glass in the row to query.
     * @return The amount of champagne in the specified glass, capped at 1.0.
     */
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[] currentRow = { (double) poured };

        for (int row = 0; row < query_row; row++) {
            double[] nextRow = new double[row + 2];
            for (int glass = 0; glass <= row; glass++) {
                double excess = currentRow[glass] - 1.0;
                if (excess > 0) {
                    double flow = excess / 2.0;
                    nextRow[glass] += flow;
                    nextRow[glass + 1] += flow;
                }
            }
            currentRow = nextRow;
        }

        return Math.min(1.0, currentRow[query_glass]);
    }
}