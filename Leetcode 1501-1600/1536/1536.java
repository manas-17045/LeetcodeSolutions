// Leetcode 1536: Minimum Swaps to Arrange a Binary Grid
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/
// Solved on 2nd of March, 2026
class Solution {
    /**
     * Calculates the minimum number of adjacent row swaps to arrange a binary grid
     * such that all elements above the main diagonal are zero.
     * @param grid An n x n binary grid.
     * @return The minimum swaps required, or -1 if it is impossible.
     */
    public int minSwaps(int[][] grid) {
        int n = grid.length;
        int[] trailingZeros = new int[n];
        
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 0) {
                    count++;
                } else {
                    break;
                }
            }
            trailingZeros[i] = count;
        }
        
        int totalSwaps = 0;
        
        for (int i = 0; i < n; i++) {
            int targetZeros = n - 1 - i;
            int currentRow = i;
            
            while (currentRow < n && trailingZeros[currentRow] < targetZeros) {
                currentRow++;
            }
            
            if (currentRow == n) {
                return -1;
            }
            
            totalSwaps += currentRow - i;
            int temp = trailingZeros[currentRow];
            
            for (int k = currentRow; k > i; k--) {
                trailingZeros[k] = trailingZeros[k - 1];
            }
            trailingZeros[i] = temp;
        }
        
        return totalSwaps;
    }
}