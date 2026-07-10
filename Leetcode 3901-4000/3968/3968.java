// Leetcode 3968: Maximum Manhattan Distance After All Moves
// https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/
// Solved on 10th of July, 2026
class Solution {
    /**
     * Returns the maximum Manhattan distance after replacing each wildcard with
     * 'L', 'R', 'U', or 'D'.
     * 
     * @param moves The string of moves.
     * @return The maximum Manhattan distance.
     */
    public int maxDistance(String moves) {
        int x = 0;
        int y = 0;
        int wildcards = 0;
        for (int i = 0; i < moves.length(); i++) {
            char c = moves.charAt(i);
            if (c == 'U') {
                y++;
            } else if (c == 'D') {
                y--;
            } else if (c == 'R') {
                x++;
            } else if (c == 'L') {
                x--;
            } else if (c == '_') {
                wildcards++;
            }
        }
        return Math.abs(x) + Math.abs(y) + wildcards;
    }
}