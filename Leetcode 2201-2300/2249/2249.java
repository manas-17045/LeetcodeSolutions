// Leetcode 2249: Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/
// Solved on 8th of November, 2025
class Solution {
    /**
     * Counts the total number of unique lattice points (points with integer coordinates) that fall within or on the boundary of any of the given circles.
     *
     * @param circles A 2D array where each `circles[i] = [xi, yi, ri]` represents a circle with center `(xi, yi)` and radius `ri`.
     * @return The total number of unique lattice points covered by at least one circle.
     */
    public int countLatticePoints(int[][] circles) {
        int minX = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;
        int minY = Integer.MAX_VALUE;
        int maxY = Integer.MIN_VALUE;
        for (int[] c : circles) {
            int cx = c[0];
            int cy = c[1];
            int r = c[2];
            minX = Math.min(minX, cx - r);
            maxX = Math.max(maxX, cx + r);
            minY = Math.min(minY, cy - r);
            maxY = Math.max(maxY, cy + r);
        }
        int width = maxX - minX + 1;
        int height = maxY - minY + 1;
        boolean[][] seen = new boolean[width][height];
        int count = 0;
        for (int[] c : circles) {
            int cx = c[0];
            int cy = c[1];
            int r = c[2];
            int r2 = r * r;
            int x1 = cx - r;
            int x2 = cx + r;
            int y1 = cy - r;
            int y2 = cy + r;
            if (x1 < minX) x1 = minX;
            if (x2 > maxX) x2 = maxX;
            if (y1 < minY) y1 = minY;
            if (y2 > maxY) y2 = maxY;
            for (int x = x1; x <= x2; x++) {
                int dx = x - cx;
                int dx2 = dx * dx;
                int xi = x - minX;
                for (int y = y1; y <= y2; y++) {
                    int yi = y - minY;
                    if (!seen[xi][yi]) {
                        int dy = y - cy;
                        if (dx2 + dy * dy <= r2) {
                            seen[xi][yi] = true;
                            count++;
                        }
                    }
                }
            }
        }
        return count;
    }
}