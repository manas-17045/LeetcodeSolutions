// Leetcode 2139: Minimum Moves to Reach Target Score
// https://leetcode.com/problems/minimum-moves-to-reach-target-score/
// Solved on 26th of February, 2026
class Solution {
    /**
     * Calculates the minimum number of moves to reach the target score starting from 1.
     * You can either increment by 1 or double the current value (if maxDoubles > 0).
     * 
     * @param target The goal integer to reach.
     * @param maxDoubles The maximum number of times the doubling operation can be used.
     * @return The minimum number of moves required to reach the target.
     */
    public int minMoves(int target, int maxDoubles) {
        int moves = 0;
        while (target > 1) {
            if (maxDoubles == 0) {
                moves += target - 1;
                break;
            }
            if (target % 2 == 0) {
                target /= 2;
                maxDoubles--;
            } else {
                target--;
            }
            moves++;
        }
        return moves;
    }
}