// Leetcode 2463: Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/
// Solved on 14th of April, 2026
import java.util.Collections;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class Solution {
    /**
     * Calculates the minimum total distance traveled by all robots to reach a factory.
     * 
     * @param robot A list of integers representing the positions of the robots.
     * @param factory A 2D integer array where factory[i] = [position_i, limit_i].
     * @return The minimum total distance traveled by all robots.
     */
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        Collections.sort(robot);
        Arrays.sort(factory, (a, b) -> Integer.compare(a[0], b[0]));
        
        List<Integer> factoryPositions = new ArrayList<>();
        for (int[] currentFactory : factory) {
            int limit = Math.min(currentFactory[1], robot.size());
            for (int i = 0; i < limit; i++) {
                factoryPositions.add(currentFactory[0]);
            }
        }
        
        long[] minDistance = new long[robot.size() + 1];
        long maxVal = 1000000000000000000L;
        Arrays.fill(minDistance, maxVal);
        minDistance[0] = 0;
        
        for (int pos : factoryPositions) {
            for (int i = robot.size(); i >= 1; i--) {
                if (minDistance[i - 1] != maxVal) {
                    long currentDistance = Math.abs((long) robot.get(i - 1) - pos);
                    minDistance[i] = Math.min(minDistance[i], minDistance[i - 1] + currentDistance);
                }
            }
        }
        
        return minDistance[robot.size()];
    }
}