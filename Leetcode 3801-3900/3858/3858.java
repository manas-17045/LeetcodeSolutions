// Leetcode 3858: Minimum Bitwise OR From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/
// Solved on 2nd of March, 2026
class Solution {
    /**
     * Calculates the minimum bitwise OR value possible by selecting one element from each row.
     *
     * @param grid A 2D integer array where one element must be chosen from each row.
     * @return The minimum possible bitwise OR sum of the chosen elements.
     */
    public int minimumOR(int[][] grid) {
        int result = 0;
        for (int i = 29; i >= 0; i--) {
            int allowed = result | ((1 << i) - 1);
            boolean isValid = true;
            for (int j = 0; j < grid.length; j++) {
                boolean rowValid = false;
                for (int k = 0; k < grid[j].length; k++) {
                    if ((grid[j][k] & ~allowed) == 0) {
                        rowValid = true;
                        break;
                    }
                }
                if (!rowValid) {
                    isValid = false;
                    break;
                }
            }
            if (!isValid) {
                result |= (1 << i);
            }
        }
        return result;
    }
}