// Leetcode 3096: Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/
// Solved on 4th of January, 2026
class Solution {
    /**
     * Calculates the minimum number of levels Daniel needs to clear to gain strictly more points than Bob.
     * @param possible An array where `possible[i]` is 1 if Daniel can clear the i-th level, and 0 otherwise.
     *                 Clearing a level with `possible[i] == 1` gives 1 point, otherwise -1 point.
     * @return The minimum number of levels Daniel needs to clear, or -1 if it's not possible.
     */
    public int minimumLevels(int[] possible) {
        int totalPoints = 0;
        for (int level : possible) {
            totalPoints += (level == 1 ? 1 : -1);
        }

        int currentPoints = 0;
        int n = possible.length;
        for (int i = 0; i < n - 1; i++) {
            currentPoints += (possible[i] == 1 ? 1 : -1);
            if (currentPoints > totalPoints - currentPoints) {
                return i + 1;
            }
        }

        return -1;
    }
}