// Leetcode 3633: Earliest Finish Time for Land and Water Rides I
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/
// Solved on 2nd of June, 2026
class Solution {
    /**
     * Calculates the earliest possible finish time for completing both a land ride and a water ride.
     *
     * @param landStartTime   An array where landStartTime[i] is the start time of the i-th land ride.
     * @param landDuration    An array where landDuration[i] is the duration of the i-th land ride.
     * @param waterStartTime  An array where waterStartTime[i] is the start time of the i-th water ride.
     * @param waterDuration   An array where waterDuration[i] is the duration of the i-th water ride.
     * @return The minimum time at which both rides can be completed.
     */
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int minLandFirstFinish = Integer.MAX_VALUE;
        for (int i = 0; i < landStartTime.length; i++) {
            int currentFinish = landStartTime[i] + landDuration[i];
            if (currentFinish < minLandFirstFinish) {
                minLandFirstFinish = currentFinish;
            }
        }

        int minWaterFirstFinish = Integer.MAX_VALUE;
        for (int i = 0; i < waterStartTime.length; i++) {
            int currentFinish = waterStartTime[i] + waterDuration[i];
            if (currentFinish < minWaterFirstFinish) {
                minWaterFirstFinish = currentFinish;
            }
        }

        int minTotalFinish = Integer.MAX_VALUE;

        for (int i = 0; i < waterStartTime.length; i++) {
            int totalFinish = Math.max(minLandFirstFinish, waterStartTime[i]) + waterDuration[i];
            if (totalFinish < minTotalFinish) {
                minTotalFinish = totalFinish;
            }
        }

        for (int i = 0; i < landStartTime.length; i++) {
            int totalFinish = Math.max(minWaterFirstFinish, landStartTime[i]) + landDuration[i];
            if (totalFinish < minTotalFinish) {
                minTotalFinish = totalFinish;
            }
        }

        return minTotalFinish;
    }
}