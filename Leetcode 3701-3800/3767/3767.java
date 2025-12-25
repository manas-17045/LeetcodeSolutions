// Leetcode 3767: Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/
// Solved on 25th of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Maximizes points after choosing k tasks.
     * @param technique1 An array representing points from technique 1 for each task.
     * @param technique2 An array representing points from technique 2 for each task.
     * @param k The number of tasks to choose.
     * @return The maximum total points achievable.
     */
    public long maxPoints(int[] technique1, int[] technique2, int k) {
        int n = technique1.length;
        long totalPoints = 0;
        int[] diff = new int[n];

        for (int i = 0; i < n; i++) {
            totalPoints += technique2[i];
            diff[i] = technique1[i] - technique2[i];
        }

        Arrays.sort(diff);

        for (int i = n - 1; i >= 0; i--) {
            if (k > 0) {
                totalPoints += diff[i];
                k--;
            } else {
                if (diff[i] > 0) {
                    totalPoints += diff[i];
                } else {
                    break;
                }
            }
        }

        return totalPoints;
    }
}