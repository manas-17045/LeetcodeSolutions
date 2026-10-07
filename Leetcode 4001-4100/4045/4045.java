// Leetcode 4045: Count Robot Groups
// https://leetcode.com/problems/count-robot-groups/
// Solved on 7th of October, 2026
class Solution {
    /**
     * Calculates the number of robot groups remaining after all possible merges.
     *
     * @param position strictly increasing array of initial positions of the robots
     * @param speed constant speeds of each corresponding robot
     * @param distance threshold distance at or within which robots merge
     * @return the total number of robot groups after all merges conclude
     */
    public int countGroups(int[] position, int[] speed, int distance) {
        int groupCount = 0;
        int lastSpeed = 0;
        int index = position.length - 1;

        while (index >= 0) {
            int currentSpeed = speed[index];
            while (index > 0 && position[index] - position[index - 1] <= distance) {
                index--;
            }
            if (groupCount == 0 || currentSpeed <= lastSpeed) {
                groupCount++;
                lastSpeed = currentSpeed;
            }
            index--;
        }

        return groupCount;
    }
}