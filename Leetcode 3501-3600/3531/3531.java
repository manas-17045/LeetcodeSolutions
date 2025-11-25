// Leetcode 3531: Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/
// Solved on 25th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Counts the number of buildings that are "covered" by other buildings.
     * A building is considered covered if there are other buildings to its left, right, above, and below.
     * @param n The maximum coordinate value for x and y (assuming coordinates are 1-indexed up to n).
     * @param buildings A 2D array where each inner array `[x, y]` represents the coordinates of a building.
     * @return The total count of covered buildings.
     */
    public int countCoveredBuildings(int n, int[][] buildings) {
        int[] minX = new int[n + 1];
        int[] maxX = new int[n + 1];
        int[] minY = new int[n + 1];
        int[] maxY = new int[n + 1];

        Arrays.fill(minX, Integer.MAX_VALUE);
        Arrays.fill(maxX, Integer.MIN_VALUE);
        Arrays.fill(minY, Integer.MAX_VALUE);
        Arrays.fill(maxY, Integer.MIN_VALUE);

        for (int[] building : buildings) {
            int x = building[0];
            int y = building[1];

            if (x < minX[y]) {
                minX[y] = x;
            }
            if (x > maxX[y]) {
                maxX[y] = x;
            }
            if (y < minY[x]) {
                minY[x] = y;
            }
            if (y > maxY[x]) {
                maxY[x] = y;
            }
        }

        int count = 0;
        for (int[] building : buildings) {
            int x = building[0];
            int y = building[1];

            boolean hasLeft = y > minY[x];
            boolean hasRight = y < maxY[x];
            boolean hasAbove = x > minX[y];
            boolean hasBelow = x < maxX[y];

            if (hasLeft && hasRight && hasAbove && hasBelow) {
                count++;
            }
        }
        return count;
    }
}