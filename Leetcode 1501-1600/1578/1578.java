// Leetcode 1578: Minimum Time to Make Rope Colorful
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
// Solved on 3rd of November, 2025
class Solution {
    /**
     * Calculates the minimum time needed to make the rope colorful such that no two adjacent balloons have the same color.
     * @param colors A string representing the colors of the balloons.
     * @param neededTime An array where neededTime[i] is the time needed to remove the i-th balloon.
     * @return The minimum time required to make the rope colorful.
     */
    public int minCost(String colors, int[] neededTime) {
        int n = colors.length();
        int totalTime = 0;
        int maxTimeInGroup = neededTime[0];

        for (int i = 1; i < n; i++) {
            if (colors.charAt(i) == colors.charAt(i - 1)) {
                totalTime += Math.min(maxTimeInGroup, neededTime[i]);
                maxTimeInGroup = Math.max(maxTimeInGroup, neededTime[i]);
            } else {
                maxTimeInGroup = needeTime[i];
            }
        }

        return totalTime;
    }
}