// Leetcode 3550: Smallest Index With Digit Sum Equal to Index
// https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
// Solved on 24th of September, 2026
class Solution {
    /**
     * Finds the smallest index where the sum of the digits of the element
     * at that index is equal to the index itself.
     *
     * @param nums the array of integers to evaluate
     * @return the smallest matching index, or -1 if no such index exists
     */
    public int smallestIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            int digitSum = 0;

            while (current > 0) {
                digitSum += current % 10;
                current /= 10;
            }

            if (digitSum == i) {
                return i;
            }
        }

        return -1;
    }
}