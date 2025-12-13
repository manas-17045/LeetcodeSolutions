// Leetcode 3235: Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/
// Solved on 13th of December, 2025
import java.util.*;

class Solution {
    /**
     * Checks if it's possible to reach the corner (xCorner, yCorner) from (0,0) in a rectangle
     * without passing through any of the given circles.
     * @param xCorner The x-coordinate of the target corner.
     * @param yCorner The y-coordinate of the target corner.
     * @param circles A 2D array where each inner array represents a circle [x, y, radius].
     * @return True if the corner is reachable, false otherwise.
     */
    public boolean canReachCorner(int xCorner, int yCorner, int[][] circles) {
        int n = circles.length;
        
        // Check if Start (0,0) or Target (xCorner, yCorner) is strictly blocked by any circle
        for (int i = 0; i < n; i++) {
            long x = circles[i][0], y = circles[i][1], r = circles[i][2];
            if ((x - 0) * (x - 0) + (y - 0) * (y - 0) <= r * r) {
                return false;
            }
            if ((x - xCorner) * (x - xCorner) + (y - yCorner) * (y - yCorner) <= r * r) {
                return false;
            }
        }
        
        // Build graph with valid connections inside the rectangle
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // Check distance between centers
                long dx = circles[i][0] - circles[j][0];
                long dy = circles[i][1] - circles[j][1];
                long distSq = dx * dx + dy * dy;
                long rSum = circles[i][2] + circles[j][2];
                
                // Only consider checking complex intersection if they geometrically intersect
                if (distSq <= rSum * rSum) {
                    // CRITICAL: Only add edge if the intersection actually blocks the rectangle area
                    if (isConnectedInRectangle(circles[i], circles[j], xCorner, yCorner)) {
                        graph.get(i).add(j);
                        graph.get(j).add(i);
                    }
                }
            }
        }
        
        // Check for blocking chains using BFS
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            
            // Flags to track which boundaries the current component touches
            boolean touchesTop = false;
            boolean touchesBottom = false;
            boolean touchesLeft = false;
            boolean touchesRight = false;
            
            Queue<Integer> q = new LinkedList<>();
            q.add(i);
            visited[i] = true;
            
            while (!q.isEmpty()) {
                int u = q.poll();
                int[] c = circles[u];
                
                // Check intersection with rectangle boundaries
                if (overlapsSegment(c, 0, yCorner, xCorner, yCorner)) {
                    touchesTop = true;
                }
                if (overlapsSegment(c, 0, 0, xCorner, 0)) {
                    touchesBottom = true;
                }
                if (overlapsSegment(c, 0, 0, 0, yCorner)) {
                    touchesLeft = true;
                }
                if (overlapsSegment(c, xCorner, 0, xCorner, yCorner)) {
                    touchesRight = true;
                }
                
                // Check blocking conditions
                if ((touchesTop && touchesBottom) || 
                    (touchesLeft && touchesRight) || 
                    (touchesTop && touchesRight) || 
                    (touchesBottom && touchesLeft)) {
                    return false;
                }
                
                for (int v : graph.get(u)) {
                    if (!visited[v]) {
                        visited[v] = true;
                        q.add(v);
                    }
                }
            }
        }
        
        return true;
    }
    
    // Check if a circle overlaps with a line segment (used for rectangle boundary checks)
    private boolean overlapsSegment(int[] c, int x1, int y1, int x2, int y2) {
        long x = c[0], y = c[1], r = c[2];
        long cx, cy;
        // Find closest point on segment to circle center
        if (x1 == x2) {
            cx = x1;
            cy = Math.max(Math.min(y1, y2), Math.min(Math.max(y1, y2), y));
        } else {
            cx = Math.max(Math.min(x1, x2), Math.min(Math.max(x1, x2), x));
            cy = y1;
        }
        return (x - cx) * (x - cx) + (y - cy) * (y - cy) <= r * r;
    }
    
    // Check if the intersection of two circles overlaps with the rectangle interior/boundary
    private boolean isConnectedInRectangle(int[] c1, int[] c2, int X, int Y) {
        // Calculate the two intersection points of the circles
        double d2 = Math.pow(c1[0] - c2[0], 2) + Math.pow(c1[1] - c2[1], 2);
        double d = Math.sqrt(d2);
        double r1 = c1[2], r2 = c2[2];
        
        // Radical axis calculation to find intersection points
        double a = (r1 * r1 - r2 * r2 + d2) / (2 * d);
        double h = Math.sqrt(Math.max(0, r1 * r1 - a * a));
        
        // Mid-point of the chord connecting intersections
        double x2 = c1[0] + a * (c2[0] - c1[0]) / d;
        double y2 = c1[1] + a * (c2[1] - c1[1]) / d;
        
        // Intersection points
        double x3_1 = x2 + h * (c2[1] - c1[1]) / d;
        double y3_1 = y2 - h * (c2[0] - c1[0]) / d;
        double x3_2 = x2 - h * (c2[1] - c1[1]) / d;
        double y3_2 = y2 + h * (c2[0] - c1[0]) / d;
        
        // If either intersection point is inside the rectangle, they are connected inside
        if (pointInRect(x3_1, y3_1, X, Y) || pointInRect(x3_2, y3_2, X, Y)) {
            return true;
        }
        
        // If points are outside, the "lens" of intersection might still cross the rectangle edges.
        // Check overlap on all 4 edges.
        if (checkEdgeOverlap(c1, c2, 0, 0, X, true)) {
            return true;
        }
        if (checkEdgeOverlap(c1, c2, Y, 0, X, true)) {
            return true;
        }
        if (checkEdgeOverlap(c1, c2, 0, 0, Y, false)) {
            return true;
        }
        if (checkEdgeOverlap(c1, c2, X, 0, Y, false)) {
            return true;
        }
        
        return false;
    }
    
    private boolean pointInRect(double x, double y, int X, int Y) {
        return x >= 0 && x <= X && y >= 0 && y <= Y;
    }
    
    // Checks if the intervals formed by c1 and c2 on a specific line (x=val or y=val) overlap
    // within the bounds of the rectangle edge [minV, maxV]
    private boolean checkEdgeOverlap(int[] c1, int[] c2, int fixedVal, int minV, int maxV, boolean isHorizontal) {
        double[] r1 = getInterval(c1, fixedVal, isHorizontal);
        double[] r2 = getInterval(c2, fixedVal, isHorizontal);
        if (r1 == null || r2 == null) {
            return false;
        }
        
        // Clip intervals to the rectangle edge length [minV, maxV]
        double start1 = Math.max(r1[0], minV);
        double end1 = Math.min(r1[1], maxV);
        
        double start2 = Math.max(r2[0], minV);
        double end2 = Math.min(r2[1], maxV);
        
        // Check if valid clipped intervals exist and overlap
        if (start1 > end1 + 1e-9 || start2 > end2 + 1e-9) {
            return false;
        }
        return Math.max(start1, start2) <= Math.min(end1, end2) + 1e-9;
    }
    
    // Helper to find the interval of a circle on a line (y=val or x=val)
    private double[] getInterval(int[] c, int val, boolean isHorizontal) {
        long centerVal = isHorizontal ? c[1] : c[0];
        long otherVal = isHorizontal ? c[0] : c[1];
        long r = c[2];
        long dist = Math.abs(centerVal - val);
        
        if (dist > r) {
            return null;
        }
        
        double d = Math.sqrt(r * r - dist * dist);
        return new double[] {otherVal - d, otherVal + d};
    }
}