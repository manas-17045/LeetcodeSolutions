// Leetcode 4061: Minimum Queen Moves to Reach Target
// https://leetcode.com/problems/minimum-queen-moves-to-reach-target/
// Solved on 28th of October, 2026
class Solution {
    /**
     * Calculates the minimum number of moves required for a queen to reach 
     * the target square on an empty 8x8 chessboard.
     *
     * @param source An array containing the 1-indexed row and column of the starting square.
     * @param target An array containing the 1-indexed row and column of the target square.
     * @return The minimum number of queen moves to reach the target square.
     */
    public int minQueenMoves(int[] sourcem int[] target) {
        int startRow = source[0];
        int startCol = source[1];
        int targetRow = target[0];
        int targetCol = target[1];

        if (startRow == targetRow && startCol == targetCol) {
            return 0;
        }

        if (startRow == targetRow || startCol == targetCol || Math.abs(startRow - targetRow) == Math.abs(startCol - targetCol)) {
            return 1;
        }

        return 2;
    }
} 