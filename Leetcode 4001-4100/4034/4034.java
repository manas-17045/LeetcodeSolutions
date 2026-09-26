// Leetcode 4034: Minimum Bishop Moves to Reach Target
// https://leetcode.com/problems/minimum-bishops-moves-to-reach-target/
// Solved on 26th of September, 2026
class Solution {
    /**
     * Calculates the minimum number of moves required for a bishop to reach
     * the target position on an 8x8 chessboard.
     *
     * @param source an array representing the starting coordinates [row, col]
     * @param target an array representing the destination coordinates [row, col]
     * @return the minimum moves needed to land on target, or -1 if unreachable
     */
    public int minBishops(int[] source, int[] target) {
        int startRow = source[0];
        int startCol = source[1];
        int targetRow = target[0];
        int targetCol = target[1];

        if ((startRow + startCol) % 2 != (targetRow + targetCol) % 2) {
            return -1;
        }

        if (Math.abs(startRow - targetRow) == Math.abs(startCol - targetCol)) {
            return 1;
        }

        return 2;
    }
}