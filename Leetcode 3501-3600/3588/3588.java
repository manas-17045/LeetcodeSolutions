// Leetcode 3588: Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/
// Solved on 25th of November, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Finds the maximum possible area of a triangle formed by three points from the given set of coordinates.
     * The triangle must have at least one side parallel to either the x-axis or the y-axis.
     * @param coords A 2D array where each inner array `[x, y]` represents a point.
     * @return The maximum area of such a triangle, or -1 if no such triangle can be formed (e.g., less than 3 points or all points are collinear).
     */
    public long maxArea(int[][] coords) {
        long minX = Long.MAX_VALUE;
        long maxX = Long.MIN_VALUE;
        long minY = Long.MAX_VALUE;
        long maxY = Long.MIN_VALUE;
        
        Map<Integer, int[]> rowLimits = new HashMap<>();
        Map<Integer, int[]> colLimits = new HashMap<>();
        
        for (int[] point : coords) {
            int x = point[0];
            int y = point[1];
            
            if (x < minX) {
                minX = x;
            }
            if (x > maxX) {
                maxX = x;
            }
            if (y < minY) {
                minY = y;
            }
            if (y > maxY) {
                maxY = y;
            }
            
            int[] xRange = rowLimits.get(y);
            if (xRange == null) {
                xRange = new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE};
                rowLimits.put(y, xRange);
            }
            if (x < xRange[0]) {
                xRange[0] = x;
            }
            if (x > xRange[1]) {
                xRange[1] = x;
            }
            
            int[] yRange = colLimits.get(x);
            if (yRange == null) {
                yRange = new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE};
                colLimits.put(x, yRange);
            }
            if (y < yRange[0]) {
                yRange[0] = y;
            }
            if (y > yRange[1]) {
                yRange[1] = y;
            }
        }
        
        long maxArea = 0;
        
        for (Map.Entry<Integer, int[]> entry : rowLimits.entrySet()) {
            long y = entry.getKey();
            int[] range = entry.getValue();
            long currBase = range[1] - range[0];
            
            if (currBase > 0) {
                long height = Math.max(y - minY, maxY - y);
                long area = currBase * height;
                if (area > maxArea) {
                    maxArea = area;
                }
            }
        }
        
        for (Map.Entry<Integer, int[]> entry : colLimits.entrySet()) {
            long x = entry.getKey();
            int[] range = entry.getValue();
            long currBase = range[1] - range[0];
            
            if (currBase > 0) {
                long height = Math.max(x - minX, maxX - x);
                long area = currBase * height;
                if (area > maxArea) {
                    maxArea = area;
                }
            }
        }
        
        return maxArea == 0 ? -1 : maxArea;
    }
}