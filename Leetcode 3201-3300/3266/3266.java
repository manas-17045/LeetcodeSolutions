// Leetcode 3266: Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/
// Solved on 3rd of November, 2025
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the final state of an array after k multiplication operations.
     *
     * @param nums The initial array of integers.
     * @param k The number of multiplication operations to perform.
     * @param multiplier The value by which elements are multiplied.
     * @return An array representing the final state after k operations.
     */
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        if (multiplier == 1) {
            return nums;
        }

        long MOD = 1000000007;
        int n = nums.length;
        long maxVal = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) {
                return Long.compare(a[0], b[0]);
            }
            return Long.compare(a[1], b[1]);
        });

        for (int i = 0; i < n; i++) {
            long val = nums[i];
            maxVal = Math.max(maxVal, val);
            pq.offer(new long[]{val, i});
        }

        while (k > 0) {
            long[] top = pq.peek();
            if (top[0] * multiplier > maxVal) {
                break;
            }
            pq.poll();
            top[0] *= multiplier;
            pq.offer(top);
            k--;
        }

        long baseCycles = k / n;
        long extraOps = k % n;
        int[] result = new int[n];

        while (!pq.isEmpty()) {
            long[] top = pq.poll();
            long val = top[0];
            int idx = (int) top[1];

            long ops = baseCycles;
            if (extraOps > 0) {
                ops++;
                extraOps--;
            }

            long finalVal = (val % MOD * modPow(multiplier, ops, MOD)) % MOD;
            result[idx] = (int) finalVal;
        }

        return result;
    }

    private long modPow(long base, long exp, long mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }
    }
}