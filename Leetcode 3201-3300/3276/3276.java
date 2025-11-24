// Leetcode 3276: Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/
// Solved on 24th of November, 2025
import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer> uniqueValues;
    private List<List<Integer>> valueToRows;
    private int[][] memo;

    /**
     * Calculates the maximum score achievable by selecting cells in a grid.
     * @param grid The input grid, where each inner list represents a row of integer values.
     * @return The maximum score.
     */
    public int maxScore(List<List<Integer>> grid) {
        int rows = grid.size();
        valueToRows = new ArrayList<>(101);
        for (int i = 0; i <= 100; i++) {
            valueToRows.add(new ArrayList<>());
        }

        for (int i = 0; i < rows; i++) {
            for (int val : grid.get(i)) {
                if (!valueToRows.get(val).contains(i)) {
                    valueToRows.get(val).add(i);
                }
            }
        }

        uniqueValues = new ArrayList<>();
        for (int i = 100; i > 0; i--) {
            if (!valueToRows.get(i).isEmpty()) {
                uniqueValues.add(i);
            }
        }

        memo = new int[uniqueValues.size()][1 << rows];
        for (int i = 0; i < uniqueValues.size(); i++) {
            for (int j = 0; j < (1 << rows); j++) {
                memo[i][j] = -1;
            }
        }

        return findMax(0, 0);
    }

    private int findMax(int index, int mask) {
        if (index == uniqueValues.size()) {
            return 0;
        }
        if (memo[index][mask] != -1) {
            return memo[index][mask];
        }

        int currentVal = uniqueValues.get(index);
        int result = findMax(index + 1, mask);

        for (int row : valueToRows.get(currentVal)) {
            if ((mask & (1 << row)) == 0) {
                result = Math.max(result, currentVal + findMax(index + 1, mask | (1 << row)));
            }
        }

        return memo[index][mask] = result;
    }
}