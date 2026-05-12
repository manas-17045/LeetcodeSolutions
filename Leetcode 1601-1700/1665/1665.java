// Leetcode 1665: Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
// Solved on 12th of May, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum initial energy required to finish all given tasks.
     * 
     * @param tasks A 2D array where tasks[i] = [actual_i, minimum_i]
     * @return The minimum initial amount of energy needed to complete all tasks.
     */
    public int minimumEffort(int[][] tasks) {
        Arrays.sort(tasks, (a, b) -> (b[1] - b[0]) - (a[1] - a[0]));
        int totalEnergy = 0;
        int currentEnergy = 0;
        
        for (int[] task : tasks) {
            if (currentEnergy < task[1]) {
                totalEnergy += task[1] - currentEnergy;
                currentEnergy = task[1];
            }
            currentEnergy -= task[0];
        }

        return totalEnergy;
    }
}