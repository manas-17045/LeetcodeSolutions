// Leetcode 3605: Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/
// Solved on 7th of December, 2025
class Solution {
    private int[][] st;
    private int[] logs;
    private int n;

    /**
     * Calculates the minimum stability factor of an array.
     *
     * @param nums The input array of integers.
     * @param maxC The maximum number of cuts allowed.
     * @return The minimum stability factor.
     */
    public int minStable(int[] nums, int maxC) {
        n = nums.length;
        logs = new int[n + 1];
        logs[1] = 0;
        for (int i = 2; i <= n; i++) {
            logs[i] = logs[i / 2] + 1;
        }

        int k = 32 - Integer.numberOfLeadingZeros(n);
        st = new int[n][k];

        for (int i = 0; i < n; i++) {
            st[i][0] = nums[i];
        }

        for (int j = 1; j < k; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                st[i][j] = gcd(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
            }
        }

        int low = 0, high = n;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (canAchieve(mid, maxC)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }

    private boolean canAchieve(int len, int maxC) {
        int window = len + 1;
        if (window > n) {
            return true;
        }

        int cuts = 0;
        for (int i = window - 1; i < n; i++) {
            if (query(i - window + 1, i) >= 2) {
                cuts++;
                if (cuts > maxC) {
                    return false;
                }
                i += window - 1;
            }
        }
        return cuts <= maxC;
    }

    private int query(int L, int R) {
        int len = R - L + 1;
        int j = logs[len];
        return gcd(st[L][j], st[R - (1 << j) + 1][j]);
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