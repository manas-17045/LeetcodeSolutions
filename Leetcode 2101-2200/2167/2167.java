// Leetcode 2167: Minimum Time to Remove All Cars Containing Illegal Goods
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/
// Solved on 27th of November, 2025
class Solution {
    /**
     * Calculates the minimum time to remove all cars containing illegal goods.
     * The problem involves a string `s` representing cars, where '1' denotes a car with illegal goods
     * and '0' denotes a car without.
     *
     * @param s The string representing the cars.
     * @return The minimum time required to remove all cars with illegal goods.
     */
    public int minimumTime(String s) {
        int n = s.length();
        int[] left = new int[n];
        left[0] = s.charAt(0) == '1' ? 1 : 0;

        for (int i = 1; i < n; i++) {
            left[i] = Math.min(left[i - 1] + (s.charAt(i) == '1' ? 2 : 0), i + 1);
        }

        int minTime = left[n - 1];
        int right = 0;

        for (int i = n - 1; i >= 0; i--) {
            right = Math.min(right + (s.charAt(i) == '1' ? 2 : 0), n - i);
            int currentLeft = (i > 0) ? left[i - 1] : 0;
            minTime = Math.min(minTime, currentLeft + right);
        }

        return minTime;
    }
}