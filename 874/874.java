// Leetcode 874: Walking Robot Simulation
// https://leetcode.com/problems/walking-robot-simulation/
// Solved on 6th of April, 2026
import java.util.HashSet;
import java.util.Set;

class Solution {
    /**
     * Simulates the movement of a robot on an XY plane with obstacles.
     *
     * @param commands An array of integers representing movement or rotation commands.
     * @param obstacles A 2D array where each element is a coordinate [x, y] of an obstacle.
     * @return The maximum Euclidean distance squared from the origin that the robot reaches.
     */
    public int robotSim(int[] commands, int[][] obstacles) {
        Set<Long> obstacleSet = new HashSet<>();
        for (int[] obs : obstacles) {
            long hash = ((long) obs[0] << 32) | (obs[1] & 0xFFFFFFFFL);
            obstacleSet.add(hash);
        }

        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int dirIndex = 0;
        int currentX = 0;
        int currentY = 0;
        int maxDistance = 0;
        
        for (int command : commands) {
            if (command == -2) {
                dirIndex = (dirIndex + 3) % 4;
            } else if (command == -1) {
                dirIndex = (dirIndex + 1) % 4;
            } else {
                for (int step = 0; step < command; step++) {
                    int nextX = currentX + directions[dirIndex][0];
                    int nextY = currentY + directions[dirIndex][1];
                    long nextHash = ((long) nextX << 32) | (nextY & 0xFFFFFFFFL);
                    
                    if (obstacleSet.contains(nextHash)) {
                        break;
                    }
                    
                    currentX = nextX;
                    currentY = nextY;
                    int distance = currentX * currentX + currentY * currentY;
                    if (distance > maxDistance) {
                        maxDistance = distance;
                    }
                }
            }
        }
        
        return maxDistance;
    }
}