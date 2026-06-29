// Leetcide 3961: Maximize Sum of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/
// Solved on 29th of June, 2026
class Solution {
    /**
     * Computes the maximum sum of ratings for the devices.
     * 
     * @param units The input array of device ratings.
     * @return The maximum sum of ratings.
     */
    public long maxRatings(int[][] units) {
        int numColumns = units[0].length;
        if (numColumns == 1) {
            long totalRatings = 0;
            for (int[] row : units) {
                totalRatings += row[0];
            }
            return totalRatings;
        }
        long totalRatings = 0;
        int minSmallest = Integer.MAX_VALUE;
        int minSecondSmallest = Integer.MAX_VALUE;
        for (int[] row : units) {
            int smallest = Integer.MAX_VALUE;
            int secondSmallest = Integer.MAX_VALUE;
            for (int value : row) {
                if (value < smallest) {
                    secondSmallest = smallest;
                    smallest = value;
                } else if (value < secondSmallest) {
                    secondSmallest = value;
                }
            }
            totalRatings += secondSmallest;
            if (smallest < minSmallest) {
                minSmallest = smallest;
            }
            if (secondSmallest < minSecondSmallest) {
                minSecondSmallest = secondSmallest;
            }
        }
        totalRatings -= (minSecondSmallest - minSmallest);
        return totalRatings;
    }
}