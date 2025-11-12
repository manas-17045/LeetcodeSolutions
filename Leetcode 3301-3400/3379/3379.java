// Leetcode 3379: Transformed Array
// https://leetcode.com/problems/transformed-array/
// Solved on 12th of November, 2025
class Solution {
    public int[] constructTransformedArray(int[] nums) {
    /**
     * Constructs a transformed array based on the given input array `nums`.
     * For each element `nums[i]`, it calculates a target index `(i + nums[i]) % n`
     * and sets `result[i]` to `nums[target]`.
     * @param nums The input array of integers.
     * @return The transformed array.
     */
        int n = nums.length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int steps = nums[i];
            int target = (i + steps) % n;
            if (target < 0) {
                target += n;
            }
            result[i] = nums[target];
        }
        return result;
    }
}