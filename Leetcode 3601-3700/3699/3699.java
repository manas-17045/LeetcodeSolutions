// Leetcode 3699: Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/
// Solved on 20th of December, 2025
class Solution {
    /**
     * Calculates the number of "zigzag" arrays of length `n` where elements are chosen from the range `[l, r]`.
     * A zigzag array is defined as an array where elements strictly alternate between increasing and decreasing.
     * @param n The length of the zigzag array.
     * @param l The lower bound of the range (inclusive).
     * @param r The upper bound of the range (inclusive).
     * @return The total number of zigzag arrays modulo 1,000,000,007.
     */
    public int zigZagArrays(int n, int l, int r) {
        int mod = 1_000_000_007;
        int m = r - l + 1;
        
        long[] up = new long[m];
        long[] down = new long[m];
        
        for (int i = 0; i < m; i++) {
            up[i] = i;
            down[i] = m - 1 - i;
        }
        
        long[] newUp = new long[m];
        long[] newDown = new long[m];
        
        for (int k = 3; k <= n; k++) {
            long currentSum = 0;
            for (int i = 0; i < m; i++) {
                newUp[i] = currentSum;
                currentSum = (currentSum + down[i]) % mod;
            }
            
            currentSum = 0;
            for (int i = m - 1; i >= 0; i--) {
                newDown[i] = currentSum;
                currentSum = (currentSum + up[i]) % mod;
            }
            
            long[] tempUp = up;
            up = newUp;
            newUp = tempUp;
            
            long[] tempDown = down;
            down = newDown;
            newDown = tempDown;
        }
        
        long total = 0;
        for (long val : up) {
            total = (total + val) % mod;
        }
        for (long val : down) {
            total = (total + val) % mod;
        }
        
        return (int) total;
    }
}