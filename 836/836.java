// Leetcode 836: Rectangle Overlap
// https://leetcode.com/problems/rectangle-overlap/
// Solved on 14th of September, 2026
class Solution {
    /**
     * Checks whether two axis-aligned rectangles overlap with a positive intersection area.
     *
     * @param rec1 the coordinates of the first rectangle in [x1, y1, x2, y2] format
     * @param rec2 the coordinates of the second rectangle in [x1, y1, x2, y2] format
     * @return true if the rectangles overlap with positive area, false otherwise
     */
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        return rec1[0] < rec2[2] && rec1[2] > rec2[0] && rec1[1] < rec2[3] && rec1[3] > rec2[1];
    }
}