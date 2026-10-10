// Leetcode 4048: Count Values With Equally Spaced Occurrences I
// https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-i/
// Solved on 10th of October, 2026
class Solution {
    /**
     * Counts the number of distinct special integers in the given array.
     * 
     * @param nums the input array of integers
     * @return the count of special integers
     */
    public int countSpecialIntegers(int[] nums) {
        int n = nums.length;
        int[] count = new int[101];
        int[][] indices = new int[101][4];

        for (int i = 0; i < n; i++) {
            int val = nums[i];
            count[val]++;
            if (count[val] <= 3) {
                indices[val][count[val]] = i;
            }
        }

        int specialCount = 0;
        for (int val = 1; val <= 100; val++) {
            if (count[val] == 3) {
                int i1 = indices[val][1];
                int i2 = indices[val][2];
                int i3 = indices[val][3];
                if (i2 - i1 == i3 - i2) {
                    specialCount++;
                }
            }
        }

        return specialCount;
    }
}