// Leetcode 3175: Find The Forst Player to win K Games in a Row
// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/
// Solved on 3rd of January, 2025
class Solution {
    /**
     * Finds the index of the first player to win k games in a row.
     * @param skills An array of integers representing the skill level of each player.
     * @param k The number of consecutive wins required.
     * @return The index of the winning player.
     */
    public int findWinningPlayer(int[] skills, int k) {
        int winnerIndex = 0;
        int currentWins = 0;

        for (int i = 1; i < skills.length; i++) {
            if (skills[i] > skills[winnerIndex]) {
                winnerIndex = i;
                currentWins = 1;
            } else {
                currentWins++;
            }

            if (currentWins == k) {
                return winnerIndex;
            }
        }

        return winnerIndex;
    }
}