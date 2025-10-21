// Leetcode 1954: Minimum Garden Perimeter to Collect Enough Apples
// https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/
// Solved on 21st of October, 2025
class Solution {
    
    /**
     * Calculates the minimum perimeter of a square garden required to collect at least `neededApples`.
     *
     * @param neededApples The minimum number of apples to collect.
     * @return The minimum perimeter of the garden.
     */
    public long minimumPerimeter(long neededApples) {
        long lo = 0;
        long hi = 1;
        while (apples(hi) < neededApples) {
            hi <<= 1;
        }

        while (lo < hi) {
            long mid = lo + ((hi - lo) >>> 1);
            if (apples(mid) >= neededApples) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return 8L * lo;
    }

    private long apples(long n) {
        long a = n * (n + 1);
        long b = 2 * (n + 1);
        return 2L * b * a;
    }
}