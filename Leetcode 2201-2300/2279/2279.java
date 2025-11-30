// Leetcode 2279: Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
// Solved on 30th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum number of bags that can be filled to full capacity.
     * @param capacity An array representing the capacity of each bag.
     * @param rocks An array representing the number of rocks currently in each bag.
     * @param additionalRocks The total number of additional rocks available.
     * @return The maximum number of bags that can be filled to full capacity.
     */
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int n = capacity.length;
        int count = 0;

        for (int i = 0; i < n; i++) {
            capacity[i] -= rocks[i];
        }

        Arrays.sort(capacity);

        for (int i = 0; i < n; i++) {
            if (additionalRocks >= capacity[i]) {
                additionalRocks -= capacity[i];
                count++;
            } else {
                break;
            }
        }

        return count;
    }
}