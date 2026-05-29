// Leetcode 3300: Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
// Solved on 29th of May, 2026
class Solution {
    /**
     * Calculates the minimum element in the array after replacing each element 
     * with the sum of its digits.
     * 
     * @param nums An array of integers.
     * @return The minimum digit sum found among all elements in the array.
     */
    public int minElement(int[] nums) {
        int minVal = Integer.MAX_VALUE;
        for (int num : nums) {
            int currentSum = 0;
            while (num > 0) {
                currentSum += num % 10;
                num /= 10;
            }
            if (currentSum < minVal) {
                minVal = currentSum;
            }
        }
        return minVal;
    }
}