// Leetcode 3640: Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/
// Solved on 4th of February, 2026
class Solution {
    /**
     * Calculates the maximum sum of a trionic subarray.
     *
     * @param nums An array of integers.
     * @return The maximum sum of a subarray that follows the trionic pattern.
     */
    public long maxSumTrionic(int[] nums) {
        long minVal = -1_000_000_000_000_000L;
        long inc1 = nums[0];
        long inc2 = minVal;
        long dec = minVal;
        long fin = minVal;
        long maxScore = minVal;

        for (int i = 1; i < nums.length; i++) {
            long currInc1 = minVal;
            long currInc2 = minVal;
            long currDec = minVal;
            long currFin = minVal;

            if (nums[i] > nums[i - 1]) {
                currInc1 = Math.max((long) nums[i], inc1 + nums[i]);
                currInc2 = inc1 + nums[i];

                long fromDec = (dec == minVal) ? minVal : dec + nums[i];
                long fromFin = (fin == minVal) ? minVal : fin + nums[i];
                currFin = Math.max(fromDec, fromFin);
            } else if (nums[i] < nums[i - 1]) {
                currInc1 = nums[i];

                long fromInc2 = (inc2 == minVal) ? minVal : inc2 + nums[i];
                long fromDec = (dec == minVal) ? minVal : dec + nums[i];
                currDec = Math.max(fromInc2, fromDec);
            } else {
                currInc1 = nums[i];
            }

            if (currFin > maxScore) {
                maxScore = currFin;
            }

            inc1 = currInc1;
            inc2 = currInc2;
            dec = currDec;
            fin = currFin;
        }

        return maxScore;
    }
}