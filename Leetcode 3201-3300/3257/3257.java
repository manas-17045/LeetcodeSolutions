// Leetcode 3257: Maximum Value Sum by Placing Three Rooks II
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/
// Solved on 3rd of November, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Calculates the maximum value sum by placing three rooks on a chessboard.
     * The rooks must be placed such that no two rooks share the same row or column.
     * @param board A 2D integer array representing the chessboard, where board[i][j] is the value at cell (i, j).
     * @return The maximum possible sum of values from the three rooks.
     */
    public long maximumValueSum(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        List<int[]> candidates = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            int[] vals = {Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE};
            int[] cols = {-1, -1, -1};

            for (int j = 0; j < n; j++) {
                int val = board[i][j];
                if (val > vals[0]) {
                    vals[2] = vals[1];
                    cols[2] = cols[1];
                    vals[1] = vals[0];
                    cols[1] = cols[0];
                    vals[0] = val;
                    cols[0] = j;
                } else if (val > vals[1]) {
                    vals[2] = vals[1];
                    cols[2] = cols[1];
                    vals[1] = val;
                    cols[1] = j;
                } else if (val > vals[2]) {
                    vals[2] = val;
                    cols[2] = j;
                }
            }

            if (cols[0] != -1) {
                candidates.add(new int[]{vals[0], i, cols[0]});
            }
            if (cols[1] != -1) {
                candidates.add(new int[]{vals[1], i, cols[1]});
            }
            if (cols[2] != -1) {
                candidates.add(new int[]{vals[2], i, cols[2]});
            }
        }

        candidates.sort((a, b) -> Integer.compare(b[0], a[0]));

        long maxSum = Long.MIN_VALUE;
        int size = candidates.size();

        for (int i = 0; i < size; i++) {
            int[] cell1 = candidates.get(i);
            long val1 = cell1[0];
            if (val1 * 3 <= maxSum) {
                break;
            }

            for (int j = i + 1; j < size; j++) {
                int[] cell2 = candidates.get(j);
                long val2 = cell2[0];
                if (cell1[1] == cell2[1] || cell1[2] == cell2[2]) {
                    continue;
                }
                if (val1 + val2 * 2 <= maxSum) {
                    break;
                }

                for (int k = j + 1; k < size; k++) {
                    int[] cell3 = candidates.get(k);
                    long val3 = cell3[0];
                    if (val1 + val2 + val3 <= maxSum) {
                        break;
                    }

                    if (cell3[1] == cell1[1] || cell3[1] == cell2[1] || 
                        cell3[2] == cell1[2] || cell3[2] == cell2[2]) {
                            continue;
                    }

                    maxSum = Math.max(maxSum, val1 + val2 + val3);
                    break;
                }
            }
        }

        return maxSum;
    }
}