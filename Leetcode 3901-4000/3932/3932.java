// Leetcode 3932: Count K-th Roots in a Range
// https://leetcode.com/problems/count-k-th-roots-in-a-range/
// Solved on 31st of May, 2026
class Solution {
    /**
     * Counts the number of integers x such that l <= x^k <= r.
     *
     * @param l The lower bound of the range.
     * @param r The upper bound of the range.
     * @param k The exponent (root degree).
     * @return The count of integers whose k-th power falls within [l, r].
     */
    public int countKthRoots(int l, int r, int k) {
        if (k == 1) {
            return r - l + 1;
        }
        return countValid(r, k) - countValid(l - 1, k);
    }

    private int countValid(int n, int k) {
        if (n < 0) {
            return 0;
        }
        long low = 0;
        long high = 31622;
        long ans = 0;
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (isLessThanOrEqual(mid, k, n)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return (int) ans + 1;
    }

    private boolean isLessThanOrEqual(long base, int exp, int limit) {
        if (base == 0) {
            return true;
        }
        long res = 1;
        for (int i = 0; i < exp; i++) {
            if (res > limit / base) {
                return false;
            }
            res *= base;
        }
        return res <= limit;
    }
}