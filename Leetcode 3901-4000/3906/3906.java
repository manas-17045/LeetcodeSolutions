// Leetcode 3906 Count Good Integers on a Grid Path
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/
// Solved on 2nd of May, 2026
class Solution {
    /**
     * Counts the number of good integers in the range [l, r] based on a grid path.
     * 
     * @param l The lower bound of the range (inclusive).
     * @param r The upper bound of the range (inclusive).
     * @param directions A string of 'D' (Down) and 'R' (Right) representing the path on a 4x4 grid.
     * @return The total count of integers within the range that satisfy the path constraints.
     */
    public long countGoodIntegersOnPath(long l, long r, String directions) {
        boolean[] isPath = new boolean[16];
        int row = 0;
        int col = 0;
        isPath[0] = true;
        
        for (int i = 0; i < directions.length(); i++) {
            if (directions.charAt(i) == 'D') {
                row++;
            } else {
                col++;
            }
            isPath[row * 4 + col] = true;
        }
        
        return countValid(r, isPath) - countValid(l - 1, isPath);
    }

    private long countValid(long n, boolean[] isPath) {
        if (n < 0) {
            return 0;
        }
        
        int[] upper = new int[16];
        long temp = n;
        for (int i = 15; i >= 0; i--) {
            upper[i] = (int) (temp % 10);
            temp /= 10;
        }
        
        long[][][] memo = new long[16][2][10];
        for (int i = 0; i < 16; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 10; k++) {
                    memo[i][j][k] = -1;
                }
            }
        }
        
        return dfs(0, 1, 0, upper, isPath, memo);
    }

    private long dfs(int idx, int tight, int lastDigit, int[] upper, boolean[] isPath, long[][][] memo) {
        if (idx == 16) {
            return 1;
        }
        
        if (memo[idx][tight][lastDigit] != -1) {
            return memo[idx][tight][lastDigit];
        }
        
        int limit = tight == 1 ? upper[idx] : 9;
        long ways = 0;
        
        for (int d = 0; d <= limit; d++) {
            int nextTight = (tight == 1 && d == limit) ? 1 : 0;
            
            if (isPath[idx]) {
                if (d >= lastDigit) {
                    ways += dfs(idx + 1, nextTight, d, upper, isPath, memo);
                }
            } else {
                ways += dfs(idx + 1, nextTight, lastDigit, upper, isPath, memo);
            }
        }
        
        memo[idx][tight][lastDigit] = ways;
        return ways;
    }
}