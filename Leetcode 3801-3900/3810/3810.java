// Leetcode 3810: Minimum Operations to Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/
// Solved on 23rd of January, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to reach the target array.
     * @param nums The initial array of integers.
     * @param target The target array of integers.
     * @return The minimum number of operations required.
     */
    public int minOperations(int[] nums, int[] target) {
        boolean[] seen = new boolean[100001];
        int operations = 0;
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            if (current != target[i]) {
                if (!seen[current]) {
                    seen[current] = true;
                    operations++;
                }
            }
        }
        return operations;
    }
}