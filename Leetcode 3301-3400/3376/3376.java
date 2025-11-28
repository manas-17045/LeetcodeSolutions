// Leetcode 3376: Minimum Time to Break Locks I
// https://leetcode.com/problems/minimum-time-to-break-locks-i/
// Solved on 28th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum time to break all locks.
     *
     * @param strength A list of integers representing the strength of each lock.
     * @param k An integer representing a factor in the time calculation.
     * @return The minimum time required to break all locks.
     */
    public int findMinimumTime(List<Integer> strength, int k) {
        int n = strength.size();
        int limit = 1 << n;
        int[] dp = new int[limit];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int mask = 1; mask < limit; mask++) {
            int setBits = Integer.bitCount(mask);
            int x = 1 + (setBits - 1) * k;

            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    int prevMask = mask ^ (1 << i);
                    int time = (strength.get(i) + x - 1) / x;
                    dp[mask] = Math.min(dp[mask], dp[prevMask] + time);
                }
            }
        }

        return dp[limit - 1];
    }
}