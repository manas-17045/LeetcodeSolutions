// Leetcode 3671: Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/
// Solved on 23rd of November, 2025
import java.util.*;

class Solution {
    /**
     * Calculates the total "beauty" of all beautiful subsequences in the given array `nums`.
     * A subsequence is beautiful if the greatest common divisor (GCD) of its elements is 1.
     * @param nums The input array of integers.
     * @return The total beauty, modulo 1,000,000,007.
     */
    public int totalBeauty(int[] nums) {
        int maxVal = 0;
        for (int num : nums) {
            maxVal = Math.max(maxVal, num);
        }

        int[] phi = new int[maxVal + 1];
        for (int i = 0; i <= maxVal; i++) {
            phi[i] = i;
        }
        for (int i = 2; i <= maxVal; i++) {
            if (phi[i] == i) {
                for (int j = i; j <= maxVal; j += i) {
                    phi[j] -= phi[j] / i;
                }
            }
        }

        List<Integer>[] groups = new ArrayList[maxVal + 1];
        for (int i = 1; i <= maxVal; i++) {
            groups[i] = new ArrayList<>();
        }

        for (int num : nums) {
            for (int d = 1; d * d <= num; d++) {
                if (num % d == 0) {
                    groups[d].add(num);
                    if (d * d < num) {
                        groups[num / d].add(num);
                    }
                }
            }
        }

        long totalBeauty = 0;
        long mod = 1_000_000_007;

        for (int g = 1; g <= maxVal; g++) {
            if (groups[g].isEmpty()) {
                continue;
            }
            totalBeauty = (totalBeauty + countSIS(groups[g], mod) * phi[g]) % mod;
        }

        return (int) totalBeauty;
    }

    private long countSIS(List<Integer> seq, long mod) {
        int size = seq.size();
        int[] sorted = new int[size];
        for (int i = 0; i < size; i++) {
            sorted[i] = seq.get(i);
        }
        Arrays.sort(sorted);

        int uniqueCount = 0;
        for (int i = 0; i < size; i++) {
            if (i == 0 || sorted[i] != sorted[i - 1]) {
                sorted[uniqueCount++] = sorted[i];
            }
        }

        long[] bit = new long[uniqueCount + 1];
        long total = 0;

        for (int num : seq) {
            int idx = Arrays.binarySearch(sorted, 0, uniqueCount, num) + 1;
            long count = (1 + query(bit, idx - 1, mod)) % mod;
            update(bit, idx, count, mod);
            total = (total + count) % mod;
        }

        return total;
    }

    private void update(long[] bit, int idx, long val, long mod) {
        while (idx < bit.length) {
            bit[idx] = (bit[idx] + val) % mod;
            idx += idx & -idx;
        }
    }

    private long query(long[] bit, int idx, long mod) {
        long sum = 0;
        while (idx > 0) {
            sum = (sum + bit[idx]) % mod;
            idx -= idx & -idx;
        }
        return sum;
    }
}