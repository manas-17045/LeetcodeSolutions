// Leetcode 2136: Earliest Possible Day of Full Bloom
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
// Solved on 11th of December, 2025
import java.util.Arrays;

class Solution {
    private record SeedInfo(int plantTime, int growTime) {}

    /**
     * Calculates the earliest possible day all flowers can bloom.
     * @param plantTime An array where plantTime[i] is the time it takes to plant the i-th flower.
     * @param growTime An array where growTime[i] is the time it takes for the i-th flower to grow.
     * @return The earliest possible day all flowers can bloom.
     */
    public int earliestFullBloom(int[] plantTime, int[] growTime) {
        int n = plantTime.length;
        SeedInfo[] seeds = new SeedInfo[n];

        for (int i = 0; i < n; i++) {
            seeds[i] = new SeedInfo(plantTime[i], growTime[i]);
        }

        Arrays.sort(seeds, (a, b) -> b.growTime - a.growTime);

        int plantingDays = 0;
        int earliestBloomDay = 0;

        for (SeedInfo seed : seeds) {
            int finishPlantingDay = plantingDays + seed.plantTime;

            int currentSeedBloomDay = finishPlantingDay + seed.growTime;

            earliestBloomDay = Math.max(earliestBloomDay, currentSeedBloomDay);

            plantingDays = finishPlantingDay;
        }

        return earliestBloomDay;
}