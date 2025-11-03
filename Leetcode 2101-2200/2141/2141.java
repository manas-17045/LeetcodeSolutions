// Leetcode 2141: Maximum Running Time of N Computers
// https://leetcode.com/problems/maximum-running-time-of-n-computers/
// Solved on 3rd of November, 2025
class Solution {
    /**
     * Calculates the maximum running time for 'n' computers given an array of batteries.
     * @param n The number of computers.
     * @param batteries An array representing the capacity of each battery.
     * @return The maximum running time achievable for all 'n' computers.
     */
    public long maxRunTime(int n, int[] batteries) {
        long totalSum = 0;
        for (int battery : batteries) {
            totalSum += battery;
        }

        long low = 0;
        long high = totalSum / n;
        long ans = 0;

        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (isPossible(n, batteries, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }

    private boolean isPossible(int n, int[] batteries, long time) {
        if (time == 0) {
            return true;
        }
        
        long targetPower = (long) n * time;
        long availablePower = 0;

        for (long battery : batteries) {
            availablePower += Math.min(battery, time);
            if (availablePower >= targetPower) {
                return true;
            }
        }
        return availablePower >= targetPower;
    }
}