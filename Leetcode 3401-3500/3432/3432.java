// Leetcode 3432: Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/
// Solved on 5th of December, 2025
class Solution {
    /**
     * Given an integer array nums, return the number of partitions with an even sum difference.
     *
     * @param nums The input integer array.
     * @return The number of partitions with an even sum difference.
     */
    public int countPartitions(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        if (totalSum % 2 == 0) {
            return nums.length - 1;
        }
        return 0;
    }
}