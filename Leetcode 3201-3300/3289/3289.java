// Leetcode 3289: The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
// Solved on 31st of October, 2025
class Solution {
    /**
     * Finds the two sneaky numbers in the given array.
     * @param nums The input array of integers.
     * @return An array containing the two sneaky numbers.
     */
    public int[] getSneakyNumbers(int[] nums) {
        int n = nums.length - 2;
        
        for (int i = 0; i < nums.length; i++) {
            int originalValue = nums[i] % n;
            nums[originalValue] += n;
        }
        
        int[] sneakyResult = new int[2];
        int resultIndex = 0;
        
        for (int i = 0; i < n; i++) {
            int frequency = nums[i] / n;
            if (frequency == 2) {
                sneakyResult[resultIndex] = i;
                resultIndex++;
            }
        }
        
        return sneakyResult;
    }
}