// Leetcode 3001: Minimum Moves to Capture The Queen
// https://leetcode.com/problems/minimum-moves-to-capture-the-queen/
// Solved on 4th of January, 2026
class Solution {
    /**
     * Calculates the minimum number of moves required to capture the queen.
     * @param a The x-coordinate of the rook.
     * @param b The y-coordinate of the rook.
     * @param c The x-coordinate of the bishop.
     * @param d The y-coordinate of the bishop.
     * @param e The x-coordinate of the queen.
     * @param f The y-coordinate of the queen.
     * @return The minimum number of moves (1 or 2) to capture the queen.
     */
    public int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
        if (a == e) {
            boolean bishopBlocks = (c == a) && (d > Math.min(b, f)) && (d < Math.max(b, f));
            if (!bishopBlocks) {
                return 1;
            }
        }

        if (b == f) {
            boolean bishopBlocks = (d == b) && (c > Math.min(a, e)) && (c < Math.max(a, e));
            if (!bishopBlocks) {
                return 1;
            }
        }

        if (Math.abs(c - e) == Math.abs(d - f)) {
            boolean rookOnLine = Math.abs(a - c) == Math.abs(b - d);
            boolean rookBlocks = rookOnLine && (a > Math.min(c, e)) && (a < Math.max(c, e)) && (b > Math.min(d, f)) && (b < Math.max(d, f));
            if (!rookBlocks) {
                return 1;
            }
        }

        return 2;
    }
}