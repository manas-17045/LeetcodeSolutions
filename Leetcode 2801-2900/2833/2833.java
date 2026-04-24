// Leetcode 2833: Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/
// Solved on 24th of April, 2026
class Solution {
    /**
     * Calculates the furthest distance from the origin after a series of moves.
     * 
     * @param moves A string consisting of 'L', 'R', and '_', representing moves.
     * @return The maximum absolute distance from the origin.
     */
    public int furthestDistanceFromOrigin(String moves) {
        int distance = 0;
        int blankCount = 0;
        
        for (int i = 0; i < moves.length(); i++) {
            char move = moves.charAt(i);
            if (move == 'L') {
                distance--;
            } else if (move == 'R') {
                distance++;
            } else {
                blankCount++;
            }
        }
        
        return Math.abs(distance) + blankCount;
    }
}