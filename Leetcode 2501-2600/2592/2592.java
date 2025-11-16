// Leetcode 2592: Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/
// Solved on 16th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Maximizes the "greatness" of an array. The greatness is defined as the number of pairs (nums[i], nums[j])
     * such that nums[j] > nums[i] and i != j.
     * @param nums The input array of integers.
     * @return The maximum possible greatness.
     */
    public int maximizeGreatness(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        int i = 0;
        int j = 0;
        int count = 0;
        while (i < n && j < n) {
            if (nums[j] > nums[i]) {
                count++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        return count;
    }
}