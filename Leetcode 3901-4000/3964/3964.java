// Leetcode 3964: Minimum Lights to Illuminate a Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/
// Solved on 9th of July, 2026
class Solution {
    /**
     * Calculates the minimum number of additional lights needed to illuminate a road.
     * 
     * @param lights An array of integers where `lights[i]` represents the illumination range of a
     *               light at position `i`. A non-positive value indicates no light at that position.
     * @return The minimum number of additional lights required to illuminate the entire road.
     */
    public int minLights(int[] lights) {
        int n = lights.length;
        int[] diff = new int[n + 1];
        for (int i = 0; i < n; i++) {
            if (lights[i] > 0) {
                int left = Math.max(0, i - lights[i]);
                int right = Math.min(n - 1, i + lights[i]);
                diff[left]++;
                diff[right + 1]--;
            }
        }
        int additionalBulbs = 0;
        int current = 0;
        int coveredUntil = -1;
        for (int i = 0; i < n; i++) {
            current += diff[i];
            if (i <= coveredUntil) {
                continue;
            }
            if (current == 0) {
                int placement = Math.min(n - 1, i + 1);
                additionalBulbs++;
                coveredUntil = placement + 1;
            }
        }
        return additionalBulbs;
    }
}