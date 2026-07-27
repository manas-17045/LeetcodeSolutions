// Leetcode 1464: Maximum Product of Two Elements in an Array
// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
// Solved on 27th of July, 2026
class Solution {
    /**
     * Finds the maximum product of two elements in an array, after subtracting 1 from each.
     * 
     * @param nums The input array of integers.
     * @return The maximum product of two elements in the array, after subtracting 1 from each.
     */
    public int maxProduct(int[] nums) {
        int max1 = 0;
        int max2 = 0;
        
        for (int num : nums) {
            if (num > max1) {
                max2 = max1;
                max1 = num;
            } else if (num > max2) {
                max2 = num;
            }
        }
        
        return (max1 - 1) * (max2 - 1);
    }
}