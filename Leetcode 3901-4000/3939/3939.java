// Leetcode 3939: Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/
// Solved on 7th of June, 2026
class Solution {
    /**
     * Counts the number of non-adjacent subsets in a rooted tree whose sum is divisible by k.
     * 
     * @param parent An array where parent[i] is the parent of node i. parent[0] = -1.
     * @param nums An array where nums[i] is the value of node i.
     * @param k The divisor for the subset sum condition.
     * @return The number of non-empty valid subsets modulo 10^9 + 7.
     */
    public int countValidSubsets(int[] parent, int[] nums, int k) {
        int n = parent.length;
        int modVal = 1000000007;
        
        int[][] dpZero = new int[n][k];
        int[][] dpOne = new int[n][k];
        
        for (int i = 0; i < n; i++) {
            dpZero[i][0] = 1;
            dpOne[i][nums[i] % k] = 1;
        }
        
        for (int i = n - 1; i > 0; i--) {
            int p = parent[i];
            int[] nextDpZero = new int[k];
            int[] nextDpOne = new int[k];
            
            for (int x = 0; x < k; x++) {
                if (dpZero[p][x] > 0) {
                    for (int y = 0; y < k; y++) {
                        int ways = (dpZero[i][y] + dpOne[i][y]) % modVal;
                        if (ways > 0) {
                            int nextRem = (x + y) % k;
                            nextDpZero[nextRem] = (int) ((nextDpZero[nextRem] + (long) dpZero[p][x] * ways) % modVal);
                        }
                    }
                }
                
                if (dpOne[p][x] > 0) {
                    for (int y = 0; y < k; y++) {
                        if (dpZero[i][y] > 0) {
                            int nextRem = (x + y) % k;
                            nextDpOne[nextRem] = (int) ((nextDpOne[nextRem] + (long) dpOne[p][x] * dpZero[i][y]) % modVal);
                        }
                    }
                }
            }
            
            dpZero[p] = nextDpZero;
            dpOne[p] = nextDpOne;
        }
        
        int ans = (dpZero[0][0] + dpOne[0][0]) % modVal;
        ans = (ans - 1 + modVal) % modVal;
        
        return ans;
    }
}