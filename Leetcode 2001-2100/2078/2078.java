// Leetcode 2078: Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/
// Solved on 20th of April, 2026
class Solution {
    /**
     * Calculates the maximum distance between two houses with different colors.
     * 
     * @param colors An array of integers representing the color of each house.
     * @return The maximum distance between any two houses that have different colors.
     */
    public int maxDistance(int[] colors) {
        int length = colors.length;
        int leftIndex = 0;
        int rightIndex = length - 1;
        
        while (colors[leftIndex] == colors[length - 1]) {
            leftIndex++;
        }
        
        while (colors[rightIndex] == colors[0]) {
            rightIndex--;
        }
        
        return Math.max(rightIndex, length - 1 - leftIndex);
    }
}