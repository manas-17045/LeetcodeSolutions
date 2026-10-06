// Leetcode 4044: Count Good Cyclic Rotations
// https://leetcode.com/problems/count-good-cyclic-rotations/
// Solved on 6th of October, 2026
class Solution {
    /**
     * Calculates the number of cyclic rotations of the array where the sum
     * of the first half of elements is strictly greater than the sum of the second half.
     *
     * @param nums the input integer array of even length
     * @return the count of good cyclic rotations
     */
    public int countGoodRotations(int[] nums) {
        int n = nums.length;
        int halfLength = n / 2;
        long totalSum = 0;
        long firstHalfSum = 0;

        for (int i = 0; i < n; i++) {
            totalSum += nums[i];
            if (i < halfLength) {
                firstHalfSum += nums[i];
            }
        }

        int goodRotationsCount = 0;

        for (int i = 0; i < n; i++) {
            if (firstHalfSum > totalSum - firstHalfSum) {
                goodRotationsCount++;
            }
            firstHalfSum += nums[(i + halfLength) % n] - nums[i];
        }

        return goodRotationsCount;
    }
}