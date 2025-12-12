// Leetcode 3017: Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/
// Solved on 12th of December, 2025
class Solution {
    /**
     * Calculates the number of pairs of houses at a certain distance for each possible distance.
     *
     * @param n The total number of houses.
     * @param x The first special house.
     * @param y The second special house.
     * @return An array where result[k] is the number of pairs of houses with distance k+1.
     */
    public long[] countOfPairs(int n, int x, int y) {
        long[] diff = new long[n + 2];
        if (x > y) {
            int temp = x;
            x = y;
            y = temp;
        }

        for (int i = 1; i <= n; i++) {
            if (x == y || x + 1 == y) {
                add(diff, 1, n - i);
                continue;
            }

            if (i <= x) {
                int split = (x + y + 1) / 2;
                int endLine = Math.min(split, y - 1);
                add(diff, 1, endLine - i);

                int startCycle = Math.max(split + 1, i + 1);
                int endCycle = y - 1;
                if (startCycle <= endCycle) {
                    int maxD = (x - i) + 1 + (y - startCycle);
                    int minD = (x - i) + 1 + (y - endCycle);
                    add(diff, minD, maxD);
                }

                int distToY = (x - i) + 1;
                add(diff, distToY, distToY + n - y);
            } else if (i < y) {
                int split = (2 * i - x + y + 1) / 2;
                int endLine = Math.min(split, y - 1);
                add(diff, 1, endLine - i);

                int startCycle = Math.max(split + 1, i + 1);
                int endCycle = y - 1;
                if (startCycle <= endCycle) {
                    int maxD = (i - x) + 1 + (y - startCycle);
                    int minD = (i - x) + 1 + (y - endCycle);
                    add(diff, minD, maxD);
                }

                int distToY = Math.min(y - i, i - x + 1);
                add(diff, distToY, distToY + n - y);
            } else {
                add(diff, 1, n - i);
            }
        }

        long[] result = new long[n];
        long current = 0;
        for (int i = 1; i <= n; i++) {
            current += diff[i];
            result[i - 1] = current * 2;
        }
        return result;
    }

    private void add(long[] diff, int l, int r) {
        if (l > r) return;
        diff[l]++;
        diff[r + 1]--;
    }
}