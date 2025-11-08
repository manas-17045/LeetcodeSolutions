// Leetcode 2768: Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/
// Solved on 8th of November, 2025
import java.util.*;

class Solution {
    /**
     * Counts the number of 2x2 black blocks in a grid given the coordinates of black cells.
     * A 2x2 block is considered black if it contains at least one black cell.
     *
     * @param m The number of rows in the grid.
     * @param n The number of columns in the grid.
     * @param coordinates A 2D array where each `coordinates[i] = [ri, ci]` represents a black cell at `(ri, ci)`.
     * @return An array `ans` of length 5, where `ans[k]` is the number of 2x2 blocks that contain exactly `k` black cells.
     *         `ans[0]` represents the number of 2x2 blocks with 0 black cells.
     */
    public long[] countBlackBlocks(int m, int n, int[][] coordinates) {
        HashMap<Long, Integer> map = new HashMap<>();
        for (int[] c : coordinates) {
            int x = c[0];
            int y = c[1];
            for (int dx = -1; dx <= 0; dx++) {
                int i = x + dx;
                if (i < 0 || i > m - 2) continue;
                for (int dy = -1; dy <= 0; dy++) {
                    int j = y + dy;
                    if (j < 0 || j > n - 2) continue;
                    long key = (((long)i) << 32) | (j & 0xffffffffL);
                    map.put(key, map.getOrDefault(key, 0) + 1);
                }
            }
        }
        long[] result = new long[5];
        long total = (long)(m - 1) * (n - 1);
        for (int v : map.values()) result[v]++;
        long sum = result[1] + result[2] + result[3] + result[4];
        result[0] = total - sum;
        return result;
    }
}