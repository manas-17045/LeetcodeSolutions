// Leetcode 3728: Stable Subarrays With Equal Boundary and Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/
// Solved on 27th of December, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Counts the number of stable subarrays with equal boundary and interior sum.
     * A subarray capacity[l...r] is stable if capacity[l] == capacity[r] and
     * capacity[l] + capacity[r] == sum(capacity[l+1...r-1]).
     * @param capacity The input array of integers.
     * @return The total count of stable subarrays.
     */
    public long countStableSubarrays(int[] capacity) {
        int n = capacity.length;
        long[] prefixSums = new long[n];
        long runningSum = 0;
        
        for (int i = 0; i < n; i++) {
            runningSum += capacity[i];
            prefixSums[i] = runningSum;
        }
        
        Map<Integer, Map<Long, Integer>> frequencyMap = new HashMap<>();
        long count = 0;
        
        for (int i = 2; i < n; i++) {
            int prevIndex = i - 2;
            int prevVal = capacity[prevIndex];
            long prevPrefix = prefixSums[prevIndex];
            
            frequencyMap.putIfAbsent(prevVal, new HashMap<>());
            Map<Long, Integer> innerMap = frequencyMap.get(prevVal);
            innerMap.put(prevPrefix, innerMap.getOrDefault(prevPrefix, 0) + 1);
            
            int currVal = capacity[i];
            long targetPrefix = prefixSums[i - 1] - currVal;
            
            if (frequencyMap.containsKey(currVal)) {
                count += frequencyMap.get(currVal).getOrDefault(targetPrefix, 0);
            }
        }
        
        return count;
    }
}