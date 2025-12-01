// Leetcode 2870: Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
// Solved on 1st of December, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Calculates the minimum number of operations to make the array empty.
     * An operation consists of removing either 2 or 3 identical elements.
     * @param nums The input array of integers.
     * @return The minimum number of operations, or -1 if it's impossible to make the array empty.
     */
    public int minOperations(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }

        int totalOperations = 0;
        for (int count : counts.values()) {
            if (count == 1) {
                return -1;
            }
            totalOperations += (count + 2) / 3;
        }
        return totalOperations;
    }
}