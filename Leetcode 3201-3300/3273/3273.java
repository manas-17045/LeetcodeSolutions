// Leetcode 3273: Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/
// Solved on 19th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum total damage dealt to Bob to defeat all enemies.
     *
     * @param power Bob's attack power.
     * @param damage An array representing the damage each enemy deals per hit.
     * @param health An array representing the health of each enemy.
     * @return The minimum total damage Bob takes.
     */
    public long minDamage(int power, int[] damage, int[] health) {
        int n = damage.length;
        int[][] enemies = new int[n][2];
        long currentDamageSum = 0;

        for (int i = 0; i < n; i++) {
            enemies[i][0] = damage[i];
            enemies[i][1] = (health[i] + power - 1) / power;
            currentDamageSum += damage[i];
        }

        Arrays.sort(enemies, (a, b) -> {
            long valueA = (long) a[0] * b[1];
            long valueB = (long) b[0] * a[1];
            return Long.compare(valueB, valueA);
        });

        long minTotalDamage = 0;

        for (int[] enemy : enemies) {
            int dmg = enemy[0];
            int time = enemy[1];

            minTotalDamage += currentDamageSum * time;
            currentDamageSum -= dmg;
        }

        return minTotalDamage;
    }
}