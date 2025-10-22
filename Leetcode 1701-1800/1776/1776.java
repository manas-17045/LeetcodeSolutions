// Leetcode 1776: Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/
// Solved on 21st of October, 2025
import java.util.Arrays;

class Solution {
    
    /**
     * Calculates the collision times for each car.
     *
     * @param cars A 2D array where each inner array `cars[i] = [position_i, speed_i]` represents the i-th car.
     *             `position_i` is the initial position of the car, and `speed_i` is its constant speed.
     * @return An array `ans` where `ans[i]` is the time until the i-th car collides with the next car, or -1.0 if it never collides.
     */
    public double[] getCollisionTimes(int[][] cars) {
        int n = cars.length;
        double[] ans = new double[n];
        Arrays.fill(ans, -1.0);

        // Monotonic stack of indices of cars to the right that are potential collision targets
        int[] stack = new int[n];
        int top = 0;

        for (int i = n - 1; i >= 0; --i) {
            int posI = cars[i][0];
            int speedI = cars[i][1];

            // Pop candidates that are impossible to collide with or will change speed before we catch them
            while (top > 0) {
                int j = stack[top - 1];
                int posJ = cars[j][0];
                int speedJ = cars[j][1];

                // If current car is not faster, it cannot catch j
                if (speedI <= speedJ) {
                    top--;
                    continue;
                }

                // Time to catch j if j keeps its speed
                double t = (posJ - posI) / (double) (speedI - speedJ);

                // If j will collide earlier than or at t, j's speed/position will change => discard j
                if (ans[j] > 0 && t >= ans[j]) {
                    top--;
                    continue;
                }

                // Valid collision time found
                ans[i] = t;
                break;
            }

            stack[top++] = i;
        }

        return ans;
    }
}
