// Leetcode 4054: Count Shadow Pairs I
// https://leetcode.com/problems/count-shadow-pairs-i/
// Solved on 19th of October, 2026
class Solution {
    /**
     * Calculates the total number of shadow pairs in the given array.
     * A pair of indices (i, j) forms a shadow pair if i < j, nums[i] < nums[j],
     * and no intermediate index k exists such that nums[k] < nums[i] < nums[j].
     *
     * @param nums the array of integers to evaluate
     * @return the total number of shadow pairs
     */
    public long shadowPairs(int[] nums) {
        int n = nums.length;
        int[] valStack = new int[n];
        int[] countStack = new int[n];
        int top = -1;
        long totalCount = 0;
        long shadowPairCount = 0;

        for (int x: nums) {
            while (top >= 0 && valStack[top] > x) {
                totalCount -= countStack[top];
                top--;
            }

            long equalCount = 0;
            if (top >= 0 && valStack[top] == x) {
                equalCount = countStack[top];
            }

            shadowPairCount += (totalCount - equalCount);

            if (top >= 0 && valStack[top] == x) {
                countStack[top]++;
            } else {
                top++;
                valStack[top] = x;
                countStack[top] = 1;
            }
            totalCount++;
        }

        return shadowPairCount;
    }
}