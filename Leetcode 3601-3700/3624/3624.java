// Leetcode 3624: Number of Integers With Popcount-Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/
// Solved on 19th of December, 2025
class Solution {
    /**
     * Calculates the number of integers with a specific popcount-depth within given ranges,
     * and supports updates to the array of numbers.
     * @param nums An array of long integers.
     * @param queries A 2D array of queries. Each query can be of type 1 (range query) or type 2 (update query).
     * @return An array of integers, where each element is the result of a type 1 query.
     */
    public int[] popcountDepth(long[] nums, long[][] queries) {
        int n = nums.length;
        int[] preDepth = new int[65];
        preDepth[1] = 0;
        for (int i = 2; i <= 64; i++) {
            preDepth[i] = 1 + preDepth[Integer.bitCount(i)];
        }

        int[] numDepths = new int[n];
        int[][] bit = new int[n + 1][6];

        for (int i = 0; i < n; i++) {
            long val = nums[i];
            int d = 0;
            if (val > 1) {
                d = 1 + preDepth[Long.bitCount(val)];
            }
            numDepths[i] = d;
            add(bit, i + 1, d, 1);
        }

        int queryCount = 0;
        for (long[] q : queries) {
            if (q[0] == 1) {
                queryCount++;
            }
        }

        int[] result = new int[queryCount];
        int resIdx = 0;

        for (long[] q : queries) {
            int type = (int) q[0];
            if (type == 1) {
                int l = (int) q[1];
                int r = (int) q[2];
                int k = (int) q[3];
                if (k > 5) {
                    result[resIdx++] = 0;
                } else {
                    result[resIdx++] = query(bit, r + 1, k) - query(bit, l, k);
                }
            } else {
                int idx = (int) q[1];
                long val = q[2];
                int oldD = numDepths[idx];
                int newD = 0;
                if (val > 1) {
                    newD = 1 + preDepth[Long.bitCount(val)];
                }
                if (oldD != newD) {
                    add(bit, idx + 1, oldD, -1);
                    add(bit, idx + 1, newD, 1);
                    numDepths[idx] = newD;
                }
            }
        }
        return result;
    }

    private void add(int[][] bit, int index, int k, int delta) {
        while (index < bit.length) {
            bit[index][k] += delta;
            index += index & -index;
        }
    }

    private int query(int[][] bit, int index, int k) {
        int sum = 0;
        while (index > 0) {
            sum += bit[index][k];
            index -= index & -index;
        }
        return sum;
    }
}