// Leetcode 4024: Nearest Available Drone
// https://leetcode.com/problems/nearest-available-drone/
// Solved on 16h of September, 2026
class Solution {
    /**
     * Finds the index of the reachable drone closest to the target coordinates
     * based on Manhattan distance.
     *
     * @param drones a 2D array where each element contains the x-coordinate,
     *               y-coordinate, and flight range of a drone
     * @param target an array containing the x and y coordinates of the target
     * @return the smallest index of the reachable drone with the minimum distance,
     *         or -1 if no drone can reach the target
     */
    public int nearestDrone(int[][] drone, int[] target) {
        int bestIndex = -1;
        int minDistance = Integer.MAX_VALUE;
        int targetX = target[0];
        int targetY = target[1];

        for (int i = 0; i < drones.length; i++) {
            int distance = Math.abs(drones[i][0] - targetX) + Math.abs(drones[i][1] - targetY);
            if (distance <= drones[i][2] && distance < minDistance) {
                minDistance = distance;
                bestIndex = i;
            }
        }

        return bestIndex;
    }
}