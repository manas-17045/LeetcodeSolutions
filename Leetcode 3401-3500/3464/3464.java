// Leetcode 3464: Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/
// Solved on 15th of December, 2025
class Solution {
    /**
     * Maximizes the minimum distance between k points chosen from a set of given points on the boundary of a square.
     * @param side The side length of the square.
     * @param points A 2D array where each inner array represents a point [x, y] on the boundary of the square.
     * @param k The number of points to choose.
     * @return The maximum possible minimum distance between any two chosen points.
     */
    public int maxDistance(int side, int[][] points, int k) {
        // Map 2D boundary points to 1D perimeter coordinates
        long[] p = new long[points.length];
        for (int i = 0; i < points.length; i++) {
            long x = points[i][0];
            long y = points[i][1];
            
            if (y == 0) {
                p[i] = x;
            } else if (x == side) {
                p[i] = (long) side + y;
            } else if (y == side) {
                p[i] = 2L * side + (side - x);
            } else {
                p[i] = 3L * side + (side - y);
            }
        }
        
        Arrays.sort(p);
        
        // Create extended array for circular processing
        int n = p.length;
        long[] extended = new long[2 * n];
        long perimeter = 4L * side;
        for (int i = 0; i < n; i++) {
            extended[i] = p[i];
            extended[i + n] = p[i] + perimeter;
        }
        
        // Pre-allocate memory for Binary Lifting table
        int logK = 0;
        if (k > 0) {
            logK = 32 - Integer.numberOfLeadingZeros(k);
        }
        int[][] lift = new int[2 * n][logK + 1];
        int[] next = new int[2 * n];
        
        // Binary Search for the maximum minimum distance
        long low = 1, high = side; 
        long ans = 1;
        
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (check(mid, extended, n, k, lift, next, logK)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return (int) ans;
    }
    
    private boolean check(long d, long[] extended, int n, int k, int[][] lift, int[] next, int logK) {
        int len = extended.length;
        int r = 0;
        
        // Sliding window: find the nearest valid next point for each point
        for (int i = 0; i < len; i++) {
            while (r < len && extended[r] < extended[i] + d) {
                r++;
            }
            next[i] = r;
        }
        
        // Build Binary Lifting Table
        for (int i = 0; i < len; i++) {
            lift[i][0] = next[i];
        }
        // Subsequent levels
        for (int j = 1; j <= logK; j++) {
            for (int i = 0; i < len; i++) {
                int midJump = lift[i][j - 1];
                if (midJump >= len) {
                    lift[i][j] = len;
                } else {
                    lift[i][j] = lift[midJump][j - 1];
                }
            }
        }
        
        // Check all possible start points
        int jumpsNeeded = k - 1;
        for (int i = 0; i < n; i++) {
            int curr = i;
            
            // Jump k-1 times using binary lifting
            for (int bit = 0; bit <= logK; bit++) {
                if (((jumpsNeeded >> bit) & 1) != 0) {
                    curr = lift[curr][bit];
                    if (curr >= len) break;
                }
            }
            
            // If we successfully found a chain of k points (k-1 jumps)
            if (curr < len) {
                // Check if the wrap-around gap is sufficient
                if (extended[i + n] - extended[curr] >= d) {
                    return true;
                }
            }
        }
        
        return false;
    }
}