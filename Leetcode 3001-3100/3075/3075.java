// Leetcode 3075: Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/
// Solved on 25th of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum happiness sum by selecting k children.
     * @param happiness An array of integers representing the happiness of each child.
     * @param k An integer representing the number of children to select.
     * @return A long representing the maximum possible happiness sum.
     */
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);
        long totalHappiness = 0;
        int n = happiness.length;

        for (int i = 0; i < k; i++) {
            int currentHappiness = happiness[n - 1 - i];
            if (currentHappiness - i > 0) {
                totalHappiness += (currentHappiness - i);
            } else {
                break;
            }
        }

        return totalHappiness;
    }
}