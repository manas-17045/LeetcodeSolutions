// Leetcode 3040: Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/
// Solved on 4th of January, 2026
class Solution {
    /**
     * Calculates a new grid where each cell's value is the average of its 3x3 region if the region is valid,
     * otherwise it retains its original value.
     * @param image The input 2D array (grid).
     * @param threshold The maximum allowed difference between adjacent cells in a valid region.
     * @return The resulting grid with averaged regions.
     */
    public int[][] resultGrid(int[][] image, int threshold) {
        int m = image.length;
        int n = image[0].length;
        int[][] regionSum = new int[m][n];
        int[][] regionCount = new int[m][n];

        for (int i = 0; i <= m - 3; i++) {
            for (int j = 0; j <= n - 3; j++) {
                if (isValidRegion(image, i, j, threshold)) {
                    int average = calculateSubgridAverage(image, i, j);
                    for (int x = i; x < i + 3; x++) {
                        for (int y = j; y < j + 3; y++) {
                            regionSum[x][y] += average;
                            regionCount[x][y]++;
                        }
                    }
                }
            }
        }

        int[][] result = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (regionCount[i][j] == 0) {
                    result[i][j] = image[i][j];
                } else {
                    result[i][j] = regionSum[i][j] / regionCount[i][j];
                }
            }
        }
        return result;
    }

    private boolean isValidRegion(int[][] image, int r, int c, int threshold) {
        for (int i = r; i < r + 3; i++) {
            for (int j = c; j < c + 3; j++) {
                if (i < r + 2 && Math.abs(image[i][j] - image[i + 1][j]) > threshold) {
                    return false;
                }
                if (j < c + 2 && Math.abs(image[i][j] - image[i][j + 1]) > threshold) {
                    return false;
                }
            }
        }
        return true;
    }

    private int calculateSubgridAverage(int[][] image, int r, int c) {
        int sum = 0;
        for (int i = r; i < r + 3; i++) {
            for (int j = c; j < c + 3; j++) {
                sum += image[i][j];
            }
        }
        return sum / 9;
    }
}