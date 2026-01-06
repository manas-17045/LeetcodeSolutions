// Leetcode 2849: Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/
// Solved on 6th of January, 2026
class Solution {
    /**
     * Determines if a cell (fx, fy) is reachable from a starting cell (sx, sy) within a given time t.
     * Movement is allowed to any of the 8 adjacent cells (including diagonals) in one unit of time.
     * @param sx The starting x-coordinate.
     * @param sy The starting y-coordinate.
     * @param fx The finishing x-coordinate.
     * @param fy The finishing y-coordinate.
     * @param t The total time available.
     * @return True if the cell is reachable within time t, false otherwise.
     */
    public boolean isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int width = Math.abs(sx - fx);
        int height = Math.abs(sy - fy);
        int minTime = Math.max(width, height);

        if (minTime == 0) {
            return t != 1;
        }

        return t >= minTime;
    }
}