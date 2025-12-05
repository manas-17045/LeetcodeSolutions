// Leetcode 3101: Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/
// Solved on 5th of December, 2025
class Solution {
    /**
     * Counts the number of alternating subarrays in the given array.
     * An alternating subarray is one where adjacent elements are different.
     * @param nums The input array of integers.
     * @return The total count of alternating subarrays.
     */
    public long countAlternatingSubarrays(int[] nums) {
        long count = 0;
        int currentLength = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                currentLength = 1;
            } else {
                currentLength++;
            }
            count += currentLength;
        }
        return count;
    }
}