// Leetcode 3659: Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/
// Solved on 1st of November, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Checks if the given array can be partitioned into k distinct groups such that each group has an equal number of elements
     * and no element appears more than (total_elements / k) times.
     * @param nums The input array of integers.
     * @param k The number of distinct groups to partition the array into.
     * @return True if the array can be partitioned as described, false otherwise.
     */
    public boolean partitionArray(int[] nums, int k) {
        int arrayLength = nums.length;

        if (arrayLength % k != 0) {
            return false;
        }

        int maxFrequency = arrayLength / k;
        Map<Integer, Integer> frequencyMap = new HashMap<>();

        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        for (int count : frequencyMap.values()) {
            if (count > maxFrequency) {
                return false;
            }
        }

        return true;
    }
}