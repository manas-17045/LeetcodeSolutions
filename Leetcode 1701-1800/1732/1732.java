// Leetcode 1732: Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/
// Solved on 19th of June, 2026
class Solution {
    /**
     * Finds the highest altitude of a point on a road trip.
     * The road trip starts at altitude 0, and gain[i] is the net altitude gain
     * between points i and i + 1.
     *
     * @param gain An array of integers where gain[i] is the net altitude gain between points i and i + 1.
     * @return The highest altitude of a point.
     */
    public int largestAltitude(int[] gain) {
        int maxAltitude = 0;
        int currentAltitude = 0;
        for (int g : gain) {
            currentAltitude += g;
            maxAltitude = Math.max(maxAltitude, currentAltitude);
        }
        return maxAltitude;
    }
}
