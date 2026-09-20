// Leetcode 4026: Maximum Gap Between Stations
// https://leetcode.com/problems/maximum-gap-between-stations/
// Solved on 20th of Septemeber, 2026
class Solution {
    /**
     * Finds the maximum possible gap between stations assigned to consecutive workers.
     *
     * @param skill a string representing the skill requirements of each worker
     * @param station a string representing the skill supported by each station
     * @return the maximum gap between two consecutive assigned stations
     */
    public int maximumGap(String skill, String station) {
        int workerCount = skill.length();
        int stationCount = station.length();

        if (workerCount <= 1) {
            return 0;
        }

        int[] earliest = new int[workerCount];
        int stationIdx = 0;

        for (int workerIdx = 0; workerIdx < workerCount; workerIdx++) {
            char targetSkill = skill.charAt(workerIdx);
            while (stationIdx < stationCount && station.charAt(stationIdx) != targetSkill) {
                stationIdx++;
            }
            earliest[workerIdx] = stationIdx;
            stationIdx++;
        }

        int maxGap = 0;
        stationIdx = stationCount - 1;

        for (int workerIdx = workerCount - 1; workerIdx >= 1; workerIdx--) {
            char targetSkill = skill.charAt(workerIdx);
            while (stationIdx >= 0 && station.charAt(stationIdx) != targetSkill) {
                stationIdx--;
            }
            maxGap = Math.max(maxGap, stationIdx - earliest[workerIdx - 1]);
            stationIdx--;
        }

        return maxGap;
    }
}