// Leetcode 1482: Minimum Number of Days to Make m Bouquets
// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
// Solved on 11th of December, 2025
class Solution {
    /**
     * Calculates the minimum number of days required to make 'm' bouquets,
     * where each bouquet requires 'k' adjacent flowers.
     * @param bloomDay An array representing the day each flower blooms.
     * @param m The required number of bouquets.
     * @param k The number of adjacent flowers needed for one bouquet.
     * @return The minimum number of days, or -1 if it's impossible to make 'm' bouquets.
     */
    public int minDays(int[] bloomDay, int m, int k) {
        if ((long) m * k > bloomDay.length) {
            return -1;
        }

        int low = Integer.MAX_VALUE;
        int high = Integer.MIN_VALUE;

        for (int day : bloomDay) {
            low = Math.min(low, day);
            high = Math.max(high, day);
        }

        int minDays = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (canMakeBouquets(bloomDay, m, k, mid)) {
                minDays = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return minDays;
    }

    private boolean canMakeBouquets(int[] bloomDay, int m, int k, int days) {
        int bouquets = 0;
        int flowers = 0;

        for (int day : bloomDay) {
            if (day <= days) {
                flowers++;
                if (flowers == k) {
                    bouquets++;
                    flowers = 0;
                }
            } else {
                flowers = 0;
            }
        }

        return bouquets >= m;
    })
}