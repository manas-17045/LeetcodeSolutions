// Leetcode 2660: Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/
// Solved on 5th of March, 2026
class Solution {
    /**
     * Determines the winner of a bowling game based on specific scoring rules.
     *
     * @param player1 An array of integers representing the pins hit by player 1 in each turn.
     * @param player2 An array of integers representing the pins hit by player 2 in each turn.
     * @return 1 if player 1 wins, 2 if player 2 wins, and 0 if it is a draw.
     */
    public int isWinner(int[] player1, int[] player2) {
        int score1 = 0;
        int score2 = 0;
        int n = player1.length;

        for (int i = 0; i < n; i++) {
            if ((i > 0 && player1[i - 1] == 10) || (i > 1 && player1[i - 2] == 10)) {
                score1 += 2 * player1[i];
            } else {
                score1 += player1[i];
            }

            if ((i > 0 && player2[i - 1] == 10) || (i > 1 && player2[i - 2] == 10)) {
                score2 += 2 * player2[i];
            } else {
                score2 += player2[i];
            }
        }

        if (score1 > score2) {
            return 1;
        } else if (score2 > score1) {
            return 2;
        }

        return 0;
    }
}