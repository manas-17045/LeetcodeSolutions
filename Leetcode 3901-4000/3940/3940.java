// Leetcode 3940: Limit Occurrences in Sorted Array
// https://leetcode.com/problems/limit-occurrences-in-sorted-array/
// Solved on 7th of June, 2026
class Solution {
    /**
     * Limits the occurrences of each element in a sorted array to at most k.
     * 
     * @param nums The input sorted integer array.
     * @param k The maximum number of allowed occurrences for each element.
     * @return A new array containing the elements with limited occurrences.
     */
    public int[] limitOccurrences(int[] nums, int k) {
        int index = 0;
        for (int num : nums) {
            if (index < k || num != nums[index - k]) {
                nums[index] = num;
                index++;
            }
        }
        int[] result = new int[index];
        for (int i = 0; i < index; i++) {
            result[i] = nums[i];
        }
        return result;
    }
}