// Leetcode 3666: Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-equalize-binary-string/
// Solved on 27th of February, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to equalize a binary string.
     * An operation consists of choosing a substring of length k and flipping all its bits.
     *
     * @param s The input binary string consisting of '0's and '1's.
     * @param k The length of the substring to flip in each operation.
     * @return The minimum number of operations to make all characters '1', or -1 if impossible.
     */
    public int minOperations(String s, int k) {
        int n = s.length();
        int c = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') {
                c++;
            }
        }
        
        int minC = c;
        int maxC = c;
        int p = c % 2;
        int step = 0;
        
        while (step <= n + 2) {
            if (minC <= 0 && 0 <= maxC && p == 0) {
                return step;
            }
            
            int nextMin = n + 1;
            int nextMax = -1;
            
            if (minC <= k && k <= maxC) {
                nextMin = 0;
            } else {
                nextMin = Math.min(Math.abs(minC - k), Math.abs(maxC - k));
            }
            
            int targetMax = n - k;
            if (minC <= targetMax && targetMax <= maxC) {
                nextMax = n;
            } else {
                int v1 = n - Math.abs(n - minC - k);
                int v2 = n - Math.abs(n - maxC - k);
                nextMax = Math.max(v1, v2);
            }
            
            p = (p + k) % 2;
            
            if (nextMin % 2 != p) {
                nextMin++;
            }
            if (nextMax % 2 != p) {
                nextMax--;
            }
            
            if (nextMin > nextMax) {
                return -1;
            }
            
            minC = nextMin;
            maxC = nextMax;
            step++;
        }
        
        return -1;
    }
}