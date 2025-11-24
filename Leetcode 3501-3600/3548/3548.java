// Leetcode 3548: Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/
// Solved on 24th of November, 2025
class Solution {
    /**
     * Determines if a grid can be partitioned into two sub-grids with equal sums by removing a single row or column,
     * and then adjusting one of the sub-grids by adding or removing a single element to make their sums equal.
     * @param grid The input 2D integer array representing the grid.
     * @return True if such a partition is possible, false otherwise.
     */
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        long totalSum = 0;
        int[] totalCounts = new int[100001];

        for (int[] row : grid) {
            for (int val : row) {
                totalSum += val;
                totalCounts[val]++;
            }
        }

        int[] part1Counts = new int[100001];
        int[] part2Counts = totalCounts.clone();
        long sum1 = 0;

        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n; j++) {
                int val = grid[i][j];
                sum1 += val;
                part1Counts[val]++;
                part2Counts[val]--;
            }

            long sum2 = totalSum - sum1;
            long diff = Math.abs(sum1 - sum2);

            if (diff == 0) {
                return true;
            }
            if (diff > 100000) {
                continue;
            }

            int target = (int) diff;

            if (sum1 > sum2) {
                if (part1Counts[target] > 0) {
                    if ((i + 1 > 1 && n > 1) || checkEnds(grid, 0, i, 0, n - 1, target)) return true;
                }
            } else {
                if (part2Counts[target] > 0) {
                    if ((m - 1 - i > 1 && n > 1) || checkEnds(grid, i + 1, m - 1, 0, n - 1, target)) return true;
                }
            }
        }

        part1Counts = new int[100001];
        part2Counts = totalCounts.clone();
        sum1 = 0;

        for (int j = 0; j < n - 1; j++) {
            for (int i = 0; i < m; i++) {
                int val = grid[i][j];
                sum1 += val;
                part1Counts[val]++;
                part2Counts[val]--;
            }

            long sum2 = totalSum - sum1;
            long diff = Math.abs(sum1 - sum2);

            if (diff == 0) {
                return true;
            }
            if (diff > 100000) {
                continue;
            }

            int target = (int) diff;

            if (sum1 > sum2) {
                if (part1Counts[target] > 0) {
                    if ((m > 1 && j + 1 > 1) || checkEnds(grid, 0, m - 1, 0, j, target)) {
                        return true;
                    }
                }
            } else {
                if (part2Counts[target] > 0) {
                    if ((m > 1 && n - 1 - j > 1) || checkEnds(grid, 0, m - 1, j + 1, n - 1, target)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    private boolean checkEnds(int[][] grid, int rowStart, int rowEnd, int colStart, int colEnd, int target) {
        if (rowStart == rowEnd) {
            return grid[rowStart][colStart] == target || grid[rowStart][colEnd] == target;
        }
        if (colStart == colEnd) {
            return grid[rowStart][colStart] == target || grid[rowEnd][colStart] == target;
        }
        return false;
    }
}