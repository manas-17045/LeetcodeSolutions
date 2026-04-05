// Leetcode 657: Robot Return to Origin
// https://leetcode.com/problems/robot-return-to-origin/
// Solved on 5th of April, 2026
class Solution {
    /**
     * Determines if the robot returns to the origin (0,0) after a sequence of moves.
     * 
     * @param moves A string representing the sequence of moves (U, D, L, R).
     * @return true if the robot ends up at the origin, false otherwise.
     */
    public boolean judgesCircle(String moves) {
        int xCoord = 0;
        int yCoord = 0;

        for (int i = 0; i < moves.length(); i++) {
            char currentMove = moves.charAt(i);

            if (currentMove == 'R') {
                xCoord++;
            } else if (currentMove == 'L') {
                xCoord--;
            } else if (currentMove == 'U') {
                yCoord++;
            } else if (currentMove == 'D') {
                yCoord--;
            }
        }

        return xCoord == 0 && yCoord == 0;
    }
}