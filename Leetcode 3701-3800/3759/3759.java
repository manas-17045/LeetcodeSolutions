// Leetcode 3759: Count Elements With at Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/
// Solved on 26th of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Counts the number of elements in an array that have at least k greater values.
     * @param nums The input array of integers.
     * @param k The minimum number of greater values an element must have.
     * @return The count of elements satisfying the condition.
     */
    public int countElements(int[] nums, int k) {
        if (k == 0) {
            return nums.length;
        }

        Arrays.sort(nums);

        int threshold = nums[nums.length - k];
        int count = 0;

        for (int num : nums) {
            if (num < threshold) {
                count++;
            } else {
                break;
            }
        }

        return count;
    }
}