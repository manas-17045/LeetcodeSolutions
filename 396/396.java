// Leetcode 396: Rotate Function
// https://leetcode.com/problems/rotate-function/
// Solved on 1st of May, 2026
class Solution {
    /**
     * Calculates the maximum value of F(0), F(1), ..., F(n-1) for a given array.
     * 
     * @param nums An integer array of length n.
     * @return The maximum value of the rotation function.
     */
    public int maxRotateFunction(int[] nums) {
        int n = nums.length;
        int arraySum = 0;
        int functionValue = 0;
        
        for (int i = 0; i < n; i++) {
            arraySum += nums[i];
            functionValue += i * nums[i];
        }
        
        int maxValue = functionValue;
        
        for (int i = n - 1; i > 0; i--) {
            functionValue = functionValue + arraySum - n * nums[i];
            if (functionValue > maxValue) {
                maxValue = functionValue;
            }
        }
        
        return maxValue;
    }
}