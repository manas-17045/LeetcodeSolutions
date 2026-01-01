// Leetcode 3380: Maximum Area Rectangle With Point Constraints I
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/
// Solved on 1st of January, 2026
class Solution {
    /**
     * Calculates the maximum area of a rectangle formed by a subset of the given points,
     * such that no other points lie strictly inside the rectangle.
     * @param points An array of 2D integer points, where points[i] = [xi, yi].
     * @return The maximum area of such a rectangle. If no such rectangle can be formed, return -1.
     */
    public int maxRectangelArea(int[][] points) {
        int maxArea = -1;
        int n = points.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int x1 = points[i][0];
                int y1 = points[i][1];
                int x2 = points[j][0];
                int y2 = points[j][1];

                if (x1 >= x2 || y1 >= y2) {
                    continue;
                }

                boolean hasTopLeft = false;
                boolean hasBottomRight = false;

                for (int k = 0; k < n; k++) {
                    if (points[k][0] == x1 && points[k][1] == y2) {
                        hasTopLeft = true;
                    }
                    if (points[k][0] == x2 && points[k][1] == y1) {
                        hasBottomRight = true;
                    }
                }

                if (hasTopLeft && hasBottomRight) {
                    boolean isValid = true;
                    for (int k = 0; k < n; k++) {
                        int x = points[k][0];
                        int y = points[k][1];

                        if (x >= x1 && x <= x2 && y >= y1 && y <= y2) {
                            boolean isCorner = (x == x1 && y == y1) || 
                                               (x == x2 && y == y2) || 
                                               (x == x1 && y == y2) || 
                                               (x == x2 && y == y1);
                            if (!isCorner) {
                                isValid = false;
                                break;
                            }
                        }
                    }

                    if (isValid) {
                        int area = (x2 - x1) * (y2 - y1);
                        if (area > maxArea) {
                            maxArea = area;
                        }
                    }
                }
            }
        }
        return maxArea;
    }
}