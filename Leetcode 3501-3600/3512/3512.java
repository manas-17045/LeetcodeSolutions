// Leetcode 3512: Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
// Solved on 30th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of operations to make the array sum divisible by k.
     * An operation consists of changing any element to make the total sum divisible by k.
     * @param nums The input array of integers.
     * @param k The divisor.
     * @return The minimum number of operations, which is the remainder of the sum divided by k.
     */
    public int minOperations(int[] nums, int k) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum % k;
    }
}