// Leetcode 4008: Minimum Intial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/
// Solved on 30th of August, 2026
class Solution {
    /**
     * Calculates the minimum initial strength required to defeat all monsters in sequence.
     *
     * @param monsters an array where each element represents the strength of a monster
     * @param boosts a 2D array where each element contains the range and value of a temporary boost
     * @return the minimum initial strength needed to defeat all monsters
     */
    public long minInitialStrength(int[] monsters, int[][] boosts) {
        int numMonsters = monsters.length;
        long[] diff = new long[numMonsters + 1];

        for (int[] boost : boosts) {
            int left = boost[0];
            int right = boost[1];
            int value = boost[2];
            diff[left] += value;
            diff[right + 1] -= value;
        }

        long minStrength = 0;
        long currentBonus = 0;
        long prefixMonsterSum = 0;

        for (int i = 0; i < numMonsters; i++) {
            currentBonus += diff[i];
            if (monsters[i] > currentBonus) {
                long requiredStrength = prefixMonsterSum + monsters[i] - currentBonus;
                if (requiredStrength > minStrength) {
                    minStrength = requiredStrength;
                }
            }
            prefixMonsterSum += monsters[i];
        }

        return minStrength;
    }
}