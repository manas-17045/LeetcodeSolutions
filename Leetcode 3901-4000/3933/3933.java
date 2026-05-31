// Leetcode 3933: Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix/
// Solved on 31st of May, 2026
import java.util.ArrayList;

class Solution {
    /**
     * Counts the number of cells in the matrix that are local maximums within a specific range.
     * A cell (r, c) with value v is a local maximum if no cell within a distance v has a greater value.
     *
     * @param matrix A 2D integer array representing the input matrix.
     * @return The total count of local maximum cells in the matrix.
     */
    public int countLocalMaximums(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        
        ArrayList<Integer>[] cellsByValue = new ArrayList[201];
        for (int i = 0; i <= 200; i++) {
            cellsByValue[i] = new ArrayList<>();
        }
        
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                int val = matrix[r][c];
                if (val > 0) {
                    cellsByValue[val].add(r * m + c);
                }
            }
        }
        
        int[][] pref = new int[n + 1][m + 1];
        int localMaxCount = 0;
        
        for (int v = 1; v <= 200; v++) {
            if (cellsByValue[v].isEmpty()) {
                continue;
            }
            
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < m; c++) {
                    pref[r + 1][c + 1] = pref[r][c + 1] + pref[r + 1][c] - pref[r][c] + (matrix[r][c] > v ? 1 : 0);
                }
            }
            
            for (int packed : cellsByValue[v]) {
                int r = packed / m;
                int c = packed % m;
                
                int r1 = Math.max(0, r - v);
                int r2 = Math.min(n - 1, r + v);
                int c1 = Math.max(0, c - v);
                int c2 = Math.min(m - 1, c + v);
                
                int count = pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1];
                
                if (r - v >= 0 && c - v >= 0 && matrix[r - v][c - v] > v) {
                    count--;
                }
                if (r - v >= 0 && c + v < m && matrix[r - v][c + v] > v) {
                    count--;
                }
                if (r + v < n && c - v >= 0 && matrix[r + v][c - v] > v) {
                    count--;
                }
                if (r + v < n && c + v < m && matrix[r + v][c + v] > v) {
                    count--;
                }
                
                if (count == 0) {
                    localMaxCount++;
                }
            }
        }
        
        return localMaxCount;
    }
}