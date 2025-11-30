// Leetcode 1981: Minimize the Difference Between Target and Chosen Elements
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/
// Solved on 30th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Minimizes the difference between a target value and the sum of chosen elements from a matrix.
     * @param mat The input matrix where each row contains integers.
     * @param target The target integer value.
     * @return The minimum absolute difference between the target and any possible sum.
     */
    public int minimizeTheDifference(int[][] mat, int target) {
        boolean[] reachable = new boolean[target + 1];
        reachable[0] = true;
        int minGreater = Integer.MAX_VALUE;

        for (int[] row : mat) {
            Arrays.sort(row);
            boolean[] nextReachable = new boolean[target + 1];
            int nextMinGreater = Integer.MAX_VALUE;

            for (int s = 0; s <= target; s++) {
                if (!reachable[s]) {
                    continue;
                }

                for (int num : row) {
                    int sum = s + num;
                    if (sum <= target) {
                        nextReachable[sum] = true;
                    } else {
                        nextMinGreater = Math.min(nextMinGreater, sum);
                        break;
                    }
                }
            }

            if (minGreater != Integer.MAX_VALUE) {
                nextMinGreater = Math.min(nextMinGreater, minGreater + row[0]);
            }

            reachable = nextReachable;
            minGreater = nextMinGreater;
        }

        int minDiff = Integer.MAX_VALUE;
        if (minGreater != Integer.MAX_VALUE) {
            minDiff = minGreater - target;
        }

        for (int s = target; s >= 0; s--) {
            if (reachable[s]) {
                minDiff = Math.min(minDiff, target - s);
                break;
            }
        }

        return minDiff;
    }
}