// Leetcode 1927: Sum Game
// https://leetcode.com/problems/sum-game/
// Solved on 23rd of August, 2026
class Solution {
    /**
     * Determines if the first player has a winning strategy in the Sum Game.
     * 
     * @param num A string representing the initial state of the game.
     * @return True if the first player has a winning strategy, false otherwise.
     */
    public boolean sumGame(String num) {
        int balance = 0;
        int halfLength = num.length() / 2;
        for (int i = 0; i < halfLength; i++) {
            char leftChar = num.charAt(i);
            char rightChar = num.charAt(i + halfLength);

            if (leftChar == '?') {
                balance += 9;
            } else {
                balance += (leftChar - '0') * 2;
            }

            if (rightChar == '?') {
                balance -= 9;
            } else {
                balance -= (rightChar - '0') * 2;
            }
        }
        return balance != 0;
    }
}