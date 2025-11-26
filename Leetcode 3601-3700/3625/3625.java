// Leetcode 3625: Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/
// Solved on 26th of November, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Counts the number of trapezoids (including parallelograms) formed by a given set of points.
     * A trapezoid is defined by two parallel sides and two non-parallel sides.
     * @param points An array of 2D integer points, where points[i] = [xi, yi].
     * @return The total number of trapezoids.
     */
    public int countTrapezoids(int[][] points) {
        int n = points.length;
        if (n < 4) {
            return 0;
        }

        Map<Integer, Map<Long, Integer>> slopeMap = new HashMap<>();
        Map<Integer, Map<Integer, Integer>> midMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int dx = points[i][0] - points[j][0];
                int dy = points[i][1] - points[j][1];

                int g = gcd(Math.abs(dx), Math.abs(dy));
                dx /= g;
                dy /= g;

                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dx = -dx;
                    dy = -dy;
                }

                int slopeKey = (dx << 16) | (dy & 0xFFFF);
                long intercept = (long) points[i][1] * dx - (long) points[i][0] * dy;

                slopeMap.computeIfAbsent(slopeKey, k -> new HashMap<>())
                        .merge(intercept, 1, Integer::sum);

                int sumX = points[i][0] + points[j][0];
                int sumY = points[i][1] + points[j][1];
                int midKey = (sumX << 16) | (sumY & 0xFFFF);

                midMap.computeIfAbsent(midKey, k -> new HashMap<>())
                      .merge(slopeKey, 1, Integer::sum);
            }
        }

        long totalTrapezoids = 0;

        for (Map<Long, Integer> lines : slopeMap.values()) {
            long currentSlopeCount = 0;
            long currentSlopeSqSum = 0;
            for (int count : lines.values()) {
                currentSlopeCount += count;
                currentSlopeSqSum += (long) count * count;
            }
            totalTrapezoids += (currentSlopeCount * currentSlopeCount - currentSlopeSqSum) / 2;
        }

        long totalParallelograms = 0;

        for (Map<Integer, Integer> slopes : midMap.values()) {
            long currentMidCount = 0;
            long currentMidSqSum = 0;
            for (int count : slopes.values()) {
                currentMidCount += count;
                currentMidSqSum += (long) count * count;
            }
            totalParallelograms += (currentMidCount * currentMidCount - currentMidSqSum) / 2;
        }

        return (int) (totalTrapezoids - totalParallelograms);
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}