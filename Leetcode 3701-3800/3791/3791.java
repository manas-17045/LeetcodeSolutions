// Leetcode 3791: Number of Balanced Integers in a Range
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/
// Solved on 8th of January, 2026
class Solution {
    private Long[][][] memoTight;
    private Long[][] memoFull;
    private final int OFFSET = 200;

    /**
     * Counts the number of balanced integers within a given range [low, high].
     * @param low The lower bound of the range (inclusive).
     * @param high The upper bound of the range (inclusive).
     * @return The total count of balanced integers in the range.
     */
    public long countBalanced(long low, long high) {
        return count(high) - count(low - 1);
    }

    private long count(long n) {
        if (n < 10) {
            return 0;
        }
        String s = String.valueOf(n);
        int len = s.length();
        long ans = 0;

        for (int l = 2; l < len; l++) {
            memoFull = new Long[l][400];
            ans += solveFull(0, 0, l);
        }

        memoTight = new Long[len][400][2];
        ans += solveTight(0, 0, true, s);

        return ans;
    }

    private long solveFull(int index, int sum, int len) {
        if (index == len) {
            return sum == 0 ? 1 : 0;
        }
        if (memoFull[index][sum + OFFSET] != null) {
            return memoFull[index][sum + OFFSET];
        }

        long res = 0;
        int start = (index == 0) ? 1 : 0;
        
        for (int d = start; d <= 9; d++) {
            int nextSum = sum + ((index % 2 == 0) ? d : -d);
            res += solveFull(index + 1, nextSum, len);
        }

        return memoFull[index][sum + OFFSET] = res;
    }

    private long solveTight(int index, int sum, boolean isTight, String s) {
        if (index == s.length()) {
            return sum == 0 ? 1 : 0;
        }
        int tightIndex = isTight ? 1 : 0;
        if (memoTight[index][sum + OFFSET][tightIndex] != null) {
            return memoTight[index][sum + OFFSET][tightIndex];
        }

        long res = 0;
        int limit = isTight ? (s.charAt(index) - '0') : 9;
        int start = (index == 0) ? 1 : 0;

        for (int d = start; d <= limit; d++) {
            boolean nextTight = isTight && (d == limit);
            int nextSum = sum + ((index % 2 == 0) ? d : -d);
            res += solveTight(index + 1, nextSum, nextTight, s);
        }

        return memoTight[index][sum + OFFSET][tightIndex] = res;
    }
}