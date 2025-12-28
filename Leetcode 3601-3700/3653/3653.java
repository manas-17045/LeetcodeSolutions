// Leetcode 3653: XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/
// Solved on 28th of December, 2025
class Solution {
    /**
     * Applies a series of multiplication queries to a given array and then computes the XOR sum of the modified array.
     *
     * @param nums The initial array of integers.
     * @param queries A 2D array where each inner array represents a query [start, end, step, multiplier].
     * @return The XOR sum of the array after all queries have been applied.
     */
    public int xorAfterQueries(int[] nums, int[][] queries) {
        int modulus = 1000000007;
        for (int[] query : queries) {
            int start = query[0];
            int end = query[1];
            int step = query[2];
            int multiplier = query[3];
            for (int i = start; i <= end; i += step) {
                nums[i] = (int) ((long) nums[i] * multiplier % modulus);
            }
        }
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
}