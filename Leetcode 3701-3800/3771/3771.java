// Leetcode 3771: Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/
// Solved on 25th of December, 2025
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    /**
     * Calculates the total score of dungeon runs.
     * @param hp The initial health points.
     * @param damage An array of integers representing the damage dealt by each monster.
     * @param requirement An array of integers representing the health requirement to defeat each monster.
     * @return A long integer representing the total score.
     */
    public long totalScore(int hp, int[] damage, int[] requirement) {
        List<Long> values = new ArrayList<>();
        values.add(0L);
        long currentDamage = 0;
        int n = damage.length;

        for (int i = 0; i < n; i++) {
            currentDamage += damage[i];
            values.add(currentDamage);
            values.add((long) requirement[i] - hp + currentDamage);
        }

        Collections.sort(values);

        List<Long> uniqueValues = new ArrayList<>();
        if (!values.isEmpty()) {
            uniqueValues.add(values.get(0));
            for (int i = 1; i < values.size(); i++) {
                if (!values.get(i).equals(values.get(i - 1))) {
                    uniqueValues.add(values.get(i));
                }
            }
        }

        int m = uniqueValues.size();
        int[] bit = new int[m + 1];

        long totalScore = 0;
        currentDamage = 0;
        int totalElements = 0;

        int initialRank = Collections.binarySearch(uniqueValues, 0L) + 1;
        update(bit, initialRank, 1);
        totalElements++;

        for (int i = 0; i < n; i++) {
            currentDamage += damage[i];
            long target = (long) requirement[i] - hp + currentDamage;
            int targetRank = Collections.binarySearch(uniqueValues, target) + 1;

            int countGreater = totalElements - query(bit, targetRank - 1);
            totalScore += countGreater;

            int currentRank = Collections.binarySearch(uniqueValues, currentDamage) + 1;
            update(bit, currentRank, 1);
            totalElements++;
        }

        return totalScore;
    }

    private void update(int[] bit, int index, int val) {
        while (index < bit.length) {
            bit[index] += val;
            index += index & -index;
        }
    }

    private int query(int[] bit, int index) {
        int sum = 0;
        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }
        return sum;
    }
}