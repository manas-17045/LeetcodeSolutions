// Leetcode 3623: Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/
// Solved on 24th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Counts the number of trapezoids that can be formed from a given set of points.
     * A trapezoid is formed by four points (p1, p2, p3, p4) such that p1.y = p2.y < p3.y = p4.y.
     * @param points A 2D array of integers, where each inner array `[x, y]` represents a point.
     * @return The total number of trapezoids, modulo 10^9 + 7.
     */
    public int countTrapezoids(int[][] points) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));

        long ans = 0;
        long currentSum = 0;
        long mod = 1000000007;
        int n = points.length;
        int i = 0;

        while (i < n) {
            int j = i;
            while (j < n && points[j][1] == points[i][1]) {
                j++;
            }

            long count = j - i;
            if (count >= 2) {
                long pairs = (count * (count - 1)) / 2;
                ans = (ans + (pairs % mod) * currentSum) % mod;
                currentSum = (currentSum + pairs) % mod;
            }

            i = j;
        }

        return (int) ans;
    }
}