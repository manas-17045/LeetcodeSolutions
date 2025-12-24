// Leetcode 3785: Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/
// Solved on 24th of December, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Calculates the minimum number of swaps required to avoid forbidden values.
     * @param nums An array of integers.
     * @param forbidden An array of forbidden values, where forbidden[i] is forbidden for nums[i].
     * @return The minimum number of swaps needed, or -1 if it's impossible.
     */
    public int minSwaps(int[] nums, int[] forbidden) {
        int n = nums.length;
        Map<Integer, Integer> numCounts = new HashMap<>();
        Map<Integer, Integer> forbiddenCounts = new HashMap<>();
        Map<Integer, Integer> conflictCounts = new HashMap<>();
        int totalConflicts = 0;
        int maxConflictFreq = 0;

        for (int i = 0; i < n; i++) {
            int val = nums[i];
            int forbid = forbidden[i];

            numCounts.put(val, numCounts.getOrDefault(val, 0) + 1);
            forbiddenCounts.put(forbid, forbiddenCounts.getOrDefault(forbid, 0) + 1);

            if (val == forbid) {
                totalConflicts++;
                int count = conflictCounts.getOrDefault(val, 0) + 1;
                conflictCounts.put(val, count);
                if (count > maxConflictFreq) {
                    maxConflictFreq = count;
                }
            }
        }

        for (int key : numCounts.keySet()) {
            if (numCounts.get(key) + forbiddenCounts.getOrDefault(key, 0) > n) {
                return -1;
            }
        }

        if (totalConflicts == 0) {
            return 0;
        }

        return Math.max((totalConflicts + 1) / 2, maxConflictFreq);
    }
}