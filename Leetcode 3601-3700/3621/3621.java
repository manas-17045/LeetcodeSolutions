// Leetcode 3621: Number of Integers With Popcount-Depth Equal to K I
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/
// Solved on 19th of December, 2025
class Solution {
    /**
     * Calculates the number of integers x such that 1 <= x <= n and the popcount-depth of x is equal to k.
     *
     * @param n The upper bound for the integers.
     * @param k The target popcount-depth.
     * @return The count of integers with the specified popcount-depth.
     */
    public long popcountDepth(long n, int k) {
        if (k == 0) {
            return 1;
        }

        long[][] combinations = new long[65][65];
        for (int i = 0; i <= 64; i++) {
            combinations[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                combinations[i][j] = combinations[i - 1][j - 1] + combinations[i - 1][j];
            }
        }

        int[] depths = new int[65];
        depths[1] = 0;
        for (int i = 2; i <= 64; i++) {
            depths[i] = 1 + depths[Long.bitCount(i)];
        }

        long totalCount = 0;
        for (int i = 1; i <= 64; i++) {
            if (depths[i] == k - 1) {
                totalCount += countSetBits(n, i, combinations);
            }
        }

        if (k == 1) {
            totalCount--;
        }

        return totalCount;
    }

    private long countSetBits(long n, int k, long[][] combinations) {
        long count = 0;
        int setBits = 0;
        for (int i = 62; i >= 0; i--) {
            if ((n & (1L << i)) != 0) {
                int remaining = k - setBits;
                if (remaining >= 0 && remaining <= i) {
                    count += combinations[i][remaining];
                }
                setBits++;
            }
        }
        if (Long.bitCount(n) == k) {
            count++;
        }
        return count;
    }
}