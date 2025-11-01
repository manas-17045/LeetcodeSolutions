// Leetcode 3254: Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
// Solved on 1st of November, 2025
class Solution {
    public int[] resultsArray(int[] nums, int k) {
        /**
         * Calculates the "power" of k-size subarrays.
         * @param nums The input array of integers.
         * @param k The size of the subarrays.
         * @return An array where each element represents the power of the corresponding k-size subarray.
         */
        int n = nums.length;
        int[] results = new int[n - k + 1];
        
        for (int i = 0; i <= n - k; i++) {
            boolean isConsecutiveSorted = true;
            
            for (int j = i; j < i + k - 1; j++) {
                if (nums[j + 1] != nums[j] + 1) {
                    isConsecutiveSorted = false;
                    break;
                }
            }
            
            if (isConsecutiveSorted) {
                results[i] = nums[i + k - 1];
            } else {
                results[i] = -1;
            }
        }
        
        return results;
    }
}