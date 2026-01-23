// Leetcode 3809: Best Reachable Tower
// https://leetcode.com/problems/best-reachable-tower/
// Solved on 23rd of January, 2026
class Solution {
    /**
     * Finds the tower with the maximum quality within a given Manhattan distance from a center point.
     * If multiple towers have the same maximum quality, the one with the smallest x-coordinate is chosen.
     * If there's still a tie, the one with the smallest y-coordinate is chosen.
     *
     * @param towers An array of towers, where each tower is represented as [x, y, quality].
     * @param center An array [centerX, centerY] representing the center point.
     * @param radius The maximum Manhattan distance allowed from the center point.
     * @return An array [bestX, bestY] of the best tower's coordinates, or [-1, -1] if no tower is reachable.
     */
    public int[] bestTower(int[][] towers, int[] center, int radius) {
        int bestX = -1;
        int bestY = -1;
        int maxQuality = -1;
        int centerX = center[0];
        int centerY = center[1];

        for (int[] tower : towers) {
            int x = tower[0];
            int y = tower[1];
            int quality = tower[2];

            int distance = Math.abs(x - centerX) + Math.abs(y - centerY);

            if (distance <= radius) {
                if (quality > maxQuality) {
                    maxQuality = quality;
                    bestX = x;
                    bestY = y;
                } else if (quality == maxQuality) {
                    if (x < bestX || (x == bestX && y < bestY)) {
                        bestX = x;
                        bestY = y;
                    }
                }
            }
        }

        return new int[]{bestX, bestY};
    }
}