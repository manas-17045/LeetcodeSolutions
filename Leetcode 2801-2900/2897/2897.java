// Leetcode 2897: Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/
// Solved on 12th of October, 2026
class Solution {
    /**
     * Calculates the maximum possible sum of squares of k elements chosen from the 
     * array after applying bitwise operations to transfer bits optimally.
     * 
     * @param nums the list of integers to perform operations on
     * @param k the number of elements to choose for the final sum
     * @return the maximum sum of squares modulo 10^9 + 7
     */
    public int maxSum(List<Integer> nums, int k) {
        int[] bitCounts = new int[32];

        for (int num : nums) {
            for (int i = 0; i < 32; i++) {
                if ((num & (1 << i)) != 0) {
                    bitCounts[i]++;
                }
            }
        }

        long result = 0;
        long mod = 1000000007;

        for (int i = 0; i < k; i++) {
            long currentNum = 0;
            for (int j = 0; j < 32; j++) {
                if (bitCounts[j] > 0) {
                    currentNum |= (1L << j);
                    bitCounts[j]--;
                }
            }
            long square = (currentNum * currentNum) % mod;
            result = (result + square) % mod;
        }

        return (int) result;
    }
}