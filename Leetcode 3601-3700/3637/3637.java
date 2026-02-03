// Leetcode 3637: Trionic Array I
// https://leetcode.com/problems/trionic-array-i/
// Solved on 3rd of February, 2026
class Solution {
    /**
     * Checks if the given array is a Trionic Array.
     * A Trionic Array follows a specific pattern: increasing, then decreasing, then increasing.
     * @param nums An array of integers to be checked.
     * @return true if the array is Trionic, false otherwise.
     */
    public boolean isTrionic(int[] nums) {
        int n = nums.length;
        if (n < 4) {
            return false;
        }

        int i = 0;
        
        while (i < n - 1 && nums[i] < nums[i + 1]) {
            i++;
        }
        if (i == 0 || i == n - 1) {
            return false;
        }

        int p = i;
        
        while (i < n - 1 && nums[i] > nums[i + 1]) {
            i++;
        }
        if (i == p || i == n - 1) {
            return false;
        }

        while (i < n - 1 && nums[i] < nums[i + 1]) {
            i++;
        }
        
        return i == n - 1;
    }
}