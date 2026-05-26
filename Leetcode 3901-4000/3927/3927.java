// Leetcode 3927: Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/
// Solved on 26th of May, 2026
class Solution {
    /**
     * Calculates the minimum possible sum of the array by replacing each element 
     * with its smallest divisor that is also present in the original array.
     * 
     * @param nums An array of integers.
     * @return The minimum total sum of the array after replacements.
     */
    public long minArraySum(int[] nums) {
        int maxVal = 0;
        for (int num : nums) {
            if (num > maxVal) {
                maxVal = num;
            }
        }
        
        boolean[] isPresent = new boolean[maxVal + 1];
        for (int num : nums) {
            isPresent[num] = true;
        }
        
        int[] minDivisor = new int[maxVal + 1];
        for (int i = 1; i <= maxVal; i++) {
            if (isPresent[i]) {
                for (int j = i; j <= maxVal; j += i) {
                    if (isPresent[j] && minDivisor[j] == 0) {
                        minDivisor[j] = i;
                    }
                }
            }
        }
        
        long totalSum = 0;
        for (int num : nums) {
            totalSum += minDivisor[num];
        }
        
        return totalSum;
    }
}