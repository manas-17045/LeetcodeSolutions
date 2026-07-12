// Leetcode 3969: Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/
// Solved on 12th of July, 2026
class Solution {
    /**
     * Counts the number of valid subarrays.
     * 
     * @param nums The input array.
     * @param x    The target sum digit.
     * @return The number of valid subarrays.
     */
    public int countValidSubarrays(int[] nums, int x) {
        int validCount = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            long currentSum = 0;
            for (int j = i; j < n; j++) {
                currentSum += nums[j];
                if (currentSum % 10 == x) {
                    long temp = currentSum;
                    while (temp >= 10) {
                        temp /= 10;
                    }
                    if (temp == x) {
                        validCount++;
                    }
                }
            }
        }
        return validCount;
    }
}