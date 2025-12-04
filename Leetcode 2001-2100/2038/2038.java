// Leetcode 2038: Remove Colored Pieces if Both Neighbors are the Same Color
// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
// Solved on 4th of December, 2025
class Solution {
    /**
     * Determines if Alice wins the game.
     *
     * @param colors A string representing the colors of the pieces.
     * @return True if Alice wins, false otherwise.
     */
    public boolean winnerOfGame(String colors) {
        int aliceMoves = 0;
        int bobMoves = 0;

        for (int i = 1; i < colors.length() - 1; i++) {
            char current = colors.charAt(i);
            char prev = colors.charAt(i - 1);
            char next = colors.charAt(i + 1);

            if (current == 'A' && prev == 'A' && next == 'A') {
                aliceMoves++;
            } else if (current == 'B' && prev == 'B' && next == 'B') {
                bobMoves++;
            }
        }

        return aliceMoves > bobMoves;
    }
}