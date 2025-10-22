// Leetcode 2211: Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/
// Solved on 22nd of October, 2025
class Solution {
    /**
     * Counts the total number of collisions that will happen on a road.
     * Cars are moving in one direction ('L' for left, 'R' for right, 'S' for stationary).
     *
     * @param directions A string representing the initial directions of cars on the road.
     * @return The total number of collisions.
     */
    public int countCollisions(String directions) {
        int n = directions.length();
        int i = 0, j = n - 1;
        // Trim all leading 'L' (they go left and never collide)
        while (i < n && directions.charAt(i) == 'L') i++;
        // Trim all trailing 'R' (they go right and never collide)
        while (j >= 0 && directions.charAt(j) == 'R') j--;
        if (i > j) return 0; // nothing remains that can collide

        int total = j - i + 1;
        int stationary = 0;
        for (int k = i; k <= j; k++) {
            if (directions.charAt(k) == 'S') stationary++;
        }
        // Every non-'S' in the remaining segment will end up colliding at least once
        return total - stationary;
    }
}