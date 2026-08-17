// Leetcode 3996: Even Number of Knight Moves
// https://leetcode.com/problems/even-number-of-knight-moves/
// Solved on 17th of August, 2026
class Solution {
    /**
     * Checks if the target can be reached from the start in an even number of moves.
     * 
     * @param start The starting position of the knight.
     * @param target The target position of the knight.
     * @return True if the target can be reached in an even number of moves, false otherwise.
     */
    public boolean canReach(int[] start, int[] target) {
        int startSum = start[0] + start[1];
        int targetSum = target[0] + target[1];
        return (startSum % 2) == (targetSum % 2);
    }
}