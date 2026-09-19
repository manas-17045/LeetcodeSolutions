// Leetcode 1401: Circle and Rectangle Overlapping
// https://leetcode.com/problems/circle-and-rectangle-overlapping/
// Solved on 19th of September, 2026
class Solution {
    /**
     * Determines whether a circle and an axis-aligned rectangle overlap.
     *
     * @param radius the radius of the circle
     * @param xCenter the x-coordinate of the circle's center
     * @param yCenter the y-coordinate of the circle's center
     * @param x1 the x-coordinate of the rectangle's bottom-left corner
     * @param y1 the y-coordinate of the rectangle's bottom-left corner
     * @param x2 the x-coordinate of the rectangle's top-right corner
     * @param y2 the y-coordinate of the rectangle's top-right corner
     * @return true if the circle and rectangle share at least one point, false otherwise
     */
    public boolean checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int closestX = Math.max(x1, Math.min(xCenter, x2));
        int closestY = Math.max(y1, Math.min(yCenter, y2));
        int deltaX = xCenter - closestX;
        int deltaY = yCenter - closestY;
        return (deltaX * deltaX + deltaY * deltaY) <= (radius * radius);
    }
}