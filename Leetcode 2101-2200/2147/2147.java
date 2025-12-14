// Leetcode 2147: Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
// Solved on 14th of December, 2025
class Solution {
    /**
     * Calculates the number of ways to divide a long corridor.
     *
     * @param corridor The string representing the corridor.
     * @return The number of ways to divide the corridor.
     */
    public int numberOfWays(String corridor) {
        long ways = 1;
        int seats = 0;
        int previousIndex = -1;
        long modulo = 1000000007;

        for (int i = 0; i < corridor.length(); i++) {
            if (corridor.charAt(i) == 'S') {
                seats++;
                if (seats > 2 && seats % 2 == 1) {
                    ways = (ways * (i - previousIndex)) % modulo;
                }
                previousIndex = i;
            }
        }

        if (seats == 0 || seats % 2 == 1) {
            return 0;
        }

        return (int) ways;
    }
}