// Leetcode 3635: Earliest Finish Time for Land and Water Rides II
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/
// Solved on 25th of November, 2025
class Solution {
    /**
     * Calculates the earliest possible finish time for completing both a land ride and a water ride.
     * @param landStartTime An array of start times for available land rides.
     * @param landDuration An array of durations for available land rides.
     * @param waterStartTime An array of start times for available water rides.
     * @param waterDuration An array of durations for available water rides.
     * @return The earliest finish time for completing one land ride and one water ride.
     */
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int minLandFinish = Integer.MAX_VALUE;
        for (int i = 0; i < landStartTime.length; i++) {
            minLandFinish = Math.min(minLandFinish, landStartTime[i] + landDuration[i]);
        }

        int minWaterFinish = Integer.MAX_VALUE;
        for (int i = 0; i < waterStartTime.length; i++) {
            minWaterFinish = Math.min(minWaterFinish, waterStartTime[i] + waterDuration[i]);
        }

        int minTotalTime = Integer.MAX_VALUE;

        for (int i = 0; i < waterStartTime.length; i++) {
            int finishTime = Math.max(minLandFinish + waterDuration[i], waterStartTime[i] + waterDuration[i]);
            minTotalTime = Math.min(minTotalTime, finishTime);
        }

        for (int i = 0; i < landStartTime.length; i++) {
            int finishTime = Math.max(minWaterFinish + landDuration[i], landStartTime[i] + landDuration[i]);
            minTotalTime = Math.min(minTotalTime, finishTime);
        }

        return minTotalTime;
    }
}