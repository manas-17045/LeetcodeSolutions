// Leetcode 2161: Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/
// Solved on 8th of June, 2026
class Solution {
    /**
     * Partitions the array such that elements less than pivot appear first, 
     * followed by elements equal to pivot, and finally elements greater than pivot.
     * Relative order of elements in each category is preserved.
     * 
     * @param nums The input integer array to be partitioned.
     * @param pivot The integer value to partition around.
     * @return A new integer array containing the partitioned elements.
     */
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length;
        int[] result = new int[n];
        int left = 0;
        int right = n - 1;

        for (int i = 0; i < n; i++) {
            if (nums[i] < pivot) {
                result[left] = nums[i];
                left++;
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] > pivot) {
                result[right] = nums[i];
                right--;
            }
        }

        while (left <= right) {
            result[left] = pivot;
            left++;
        }

        return result;
    }
}