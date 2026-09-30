// Leetcode 4038: Count Integers Appearing in a Single Block
// https://leetcode.com/problems/count-integers-appearing-in-a-single-block/
// Solved on 30th of September, 2026
class Solution {
    /**
     * Counts the number of distinct integers in the array that appear
     * exclusively within a single contiguous block of elements.
     *
     * @param nums the input array of integers
     * @return the number of distinct special integers
     */
    public int countSpecialIntegers(int[] nums) {
        int[] blockCounts = new int[101];

        for (int i = 0; i < nums.length; i++) {
            if (i == 0 || nums[i] != nums[i - 1]) {
                blockCounts[nums[i]]++;
            }
        }

        int specialCount = 0;
        for (int count : blockCounts) {
            if (count == 1) {
                specialCount++;
            }
        }

        return specialCount;
    }
}