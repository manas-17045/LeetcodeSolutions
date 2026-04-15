// Leetcode 2515: Shortest Distance to Target String in a Circular Array
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/
// Solved on 15th of April, 2026
class Solution {
    /**
     * Finds the shortest distance to a target string in a circular array.
     *
     * @param words      The array of strings to search through.
     * @param target     The string to find the shortest distance to.
     * @param startIndex The starting index in the circular array.
     * @return The minimum number of steps to reach the target, or -1 if not found.
     */
    public int closestTarget(String[] words, String target, int startIndex) {
        int arrayLength = words.length;
        int minimumSteps = Integer.MAX_VALUE;
        for (int i = 0; i < arrayLength; i++) {
            if (words[i].equals(target)) {
                int directDistance = Math.abs(i - startIndex);
                int wrapDistance = arrayLength - directDistance;
                int shortestPath = Math.min(directDistance, wrapDistance);
                minimumSteps = Math.min(minimumSteps, shortestPath);
            }
        }
        return minimumSteps == Integer.MAX_VALUE ? -1 : minimumSteps;
    }
}