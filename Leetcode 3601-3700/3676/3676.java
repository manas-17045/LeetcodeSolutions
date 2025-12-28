// Leetcode 3676: Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/
// Solved on 28th of December, 2025
class Solution {
    /**
     * Counts the number of "bowl" subarrays.
     * A subarray is considered a "bowl" if it has a peak element that is greater than its immediate neighbors.
     * @param nums The input array of integers.
     * @return The total count of bowl subarrays.
     */
    public long bowlSubarrays(int[] nums) {
        long count = 0;
        int[] stack = new int[nums.length];
        int top = -1;

        for (int right = 0; right < nums.length; right++) {
            while (top != -1 && nums[right] > nums[stack[top]]) {
                int mid = stack[top--];
                if (top != -1) {
                    count++;
                }
            }
            stack[++top] = right;
        }

        return count;
    }
}