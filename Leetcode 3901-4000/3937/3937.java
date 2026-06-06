// Leetcode 3937: Minimum Operations to Make Array Modulo Alternating I
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/
// Solved on 6th of June, 2026
class Solution {
    /**
     * Calculates the minimum operations to make the array modulo alternating.
     * 
     * @param nums The input integer array.
     * @param k The modulo value.
     * @return The minimum number of operations required.
     */
    public int minOperations(int[] nums, int k) {
        int[] evenCosts = new int[k];
        int[] oddCosts = new int[k];
        for (int x = 0; x < k; x++) {
            for (int i = 0; i < nums.length; i += 2) {
                int rem = nums[i] % k;
                int diff1 = (x - rem + k) % k;
                int diff2 = (rem - x + k) % k;
                evenCosts[x] += Math.min(diff1, diff2);
            }
        }
        for (int y = 0; y < k; y++) {
            for (int i = 1; i < nums.length; i += 2) {
                int rem = nums[i] % k;
                int diff1 = (y - rem + k) % k;
                int diff2 = (rem - y + k) % k;
                oddCosts[y] += Math.min(diff1, diff2);
            }
        }
        int minOps = Integer.MAX_VALUE;
        for (int x = 0; x < k; x++) {
            for (int y = 0; y < k; y++) {
                if (x != y) {
                    int total = evenCosts[x] + oddCosts[y];
                    if (total < minOps) {
                        minOps = total;
                    }
                }
            }
        }
        return minOps;
    }
}