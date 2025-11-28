// Leetcode 2615: Sum of Distances
// https://leetcode.com/problems/sum-of-distances/
// Solved on 28th of November, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Calculates the sum of distances for each element in the array to all other elements with the same value.
     *
     * @param nums The input array of integers.
     * @return An array of long integers, where each element result[i] is the sum of distances between index i and all other indices j such that nums[i] == nums[j].
     */
    public long[] distance(int[] nums) {
        int n = nums.length;
        long[] result = new long[n];
        Map<Integer, Long> sumMap = new HashMap<>();
        Map<Integer, Integer> countMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int val = nums[i];
            long currentSum = sumMap.getOrDefault(val, 0L);
            int currentCount = countMap.getOrDefault(val, 0);

            result[i] += (long) i * currentCount - currentSum;

            sumMap.put(val, currentSum + i);
            countMap.put(val, currentCount + 1);
        }

        sumMap.clear();
        countMap.clear();

        for (int i = n - 1; i >= 0; i--) {
            int val = nums[i];
            long currentSum = sumMap.getOrDefault(val, 0L);
            int currentCount = countMap.getOrDefault(val, 0);

            result[i] += currentSum - (long) i * currentCount;

            sumMap.put(val, currentSum + i);
            countMap.put(val, currentCount + 1);
        }

        return result;
    }
}