// Leetcode 3779: Minimum Number of Operations to Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/
// Solved on 25th of December, 2025
import java.util.HashSet;
import java.util.Set;

class Solution {
    /**
     * Calculates the minimum number of operations to have distinct elements.
     * @param nums An array of integers.
     * @return An integer representing the minimum number of operations.
     */
    public int minOperations(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            if (seen.contains(nums[i])) {
                return (i + 3) / 3;
            }
            seen.add(nums[i]);
        }
        return 0;
    }
}