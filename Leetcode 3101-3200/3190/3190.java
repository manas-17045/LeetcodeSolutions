// Leetcode 3190: Find Minimum Operations to Make All Elements Divisible by Three
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
// Solved on 22nd of November, 2025
class Solution {
    /**
     * Calculates the minimum number of operations required to make all elements in the array divisible by three.
     * An operation consists of incrementing or decrementing an element by 1.
     * @param nums The input array of integers.
     * @return The minimum number of operations.
     */
    public int minimumOperations(int[] nums) {
        int operations = 0;
        for (int num : nums) {
            if (num % 3 != 0) {
                operations++;
            }
        }
        return operations;
    }
}