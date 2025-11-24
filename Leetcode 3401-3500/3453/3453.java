// Leetcode 3453: Separate Squares I
// https://leetcode.com/problems/separate-squares-i/
// Solved on 24th of November, 2025
class Solution {
    /**
     * Calculates the y-coordinate of a horizontal line that separates the total area of squares into two equal halves.
     *
     * @param squares A 2D array where each inner array represents a square with [x, y, side_length].
     * @return The y-coordinate of the separating line.
     */
    public double separateSquares(int[][] squares) {
        double totalArea = 0;
        double minHeight = squares[0][1];
        double maxHeight = (double)squares[0][1] + squares[0][2];

        for (int[] square : squares) {
            double y = square[1];
            double l = square[2];
            totalArea += l * l;
            minHeight = Math.min(minHeight, y);
            maxHeight = Math.max(maxHeight, y + l);
        }

        double targetArea = totalArea / 2.0;
        double low = minHeight;
        double high = maxHeight;

        for (int i = 0; i < 100; i++) {
            double mid = low + (high - low) / 2;
            double currentArea = 0;

            for (int[] square : squares) {
                double y = square[1];
                double l = square[2];
                if (mid > y) {
                    double height = Math.min(mid - y, l);
                    currentArea += height * l;
                }
            }

            if (currentArea >= targetArea) {
                high = mid;
            } else {
                low = mid;
            }
        }

        return high;
    }
}