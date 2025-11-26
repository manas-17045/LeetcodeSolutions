// Leetcode 3207: Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/
// Solved on 26th of November, 2025
class Solution {
    /**
     * Calculates the maximum points obtainable after enemy battles.
     *
     * @param enemyEnergies An array representing the energy of each enemy.
     * @param currentEnergy The player's current energy.
     * @return The maximum points the player can achieve.
     */
    public long maximumPoints(int[] enemyEnergies, int currentEnergy) {
        long totalEnergy = 0;
        int minEnergy = Integer.MAX_VALUE;

        for (int energy : enemyEnergies) {
            totalEnergy += energy;
            if (energy < minEnergy) {
                minEnergy = energy;
            }
        }

        if (currentEnergy < minEnergy) {
            return 0;
        }

        totalEnergy -= minEnergy;
        totalEnergy += currentEnergy;

        return totalEnergy / minEnergy;
    }
}