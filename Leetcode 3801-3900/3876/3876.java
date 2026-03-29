// Leetcode 3876: Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/
// Solved on 29th of March, 2026
class Solution {
    /**
     * Determines if the array can be considered uniform based on parity and minimum value.
     * @param nums1 An array of integers to evaluate.
     * @return true if the minimum value is odd or if no odd numbers exist; false otherwise.
     */
    public boolean uniformArray(int[] nums1) {
        int minValue = nums1[0];
        boolean hasOdd = false;

        for (int i = 0; i < nums1.length; i++) {
            if (nums1[i] < minValue) {
                minValue = nums1[i];
            }
            if (nums1[i] % 2 != 0) {
                hasOdd = true;
            }
        }

        if (minValue % 2 != 0) {
            return true;
        }

        return !hasOdd;
    }
}