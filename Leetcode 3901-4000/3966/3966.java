// Leetcode 3966: Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/
// Solved on 9th of July, 2026
class Solution {
    /**
     * Returns the count of good integers in the range [l, r].
     * A good integer is an integer where the absolute difference between any two
     * adjacent digits is at most k.
     * 
     * @param l The lower bound of the range (inclusive).
     * @param r The upper bound of the range (inclusive).
     * @param k The maximum allowed absolute difference between adjacent digits.
     * @return The count of good integers in the range [l, r].
    */
    public long goodIntegers(long l, long r, int k) {
        return countValid(r, k) - countValid(l - 1, k);
    }

    private long countValid(long bound, int k) {
        String numStr = String.valueOf(bound);
        int len = numStr.length();
        long[][][][] memo = new long[len][11][2][2];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < 11; j++) {
                for (int x = 0; x < 2; x++) {
                    for (int y = 0; y < 2; y++) {
                        memo[i][j][x][y] = -1;
                    }
                }
            }
        }
        return calculate(numStr, 0, 10, 1, 0, k, memo);
    }

    private long calculate(String numStr, int index, int prev, int tight, int started, int k, long[][][][] memo) {
        if (index == numStr.length()) {
            return started == 1 ? 1 : 0;
        }
        if (memo[index][prev][tight][started] != -1) {
            return memo[index][prev][tight][started];
        }
        int limit = tight == 1 ? numStr.charAt(index) - '0' : 9;
        long count = 0;
        for (int digit = 0; digit <= limit; digit++) {
            int nextTight = (tight == 1 && digit == limit) ? 1 : 0;
            int nextStarted = (started == 1 || digit > 0) ? 1 : 0;
            if (started == 0) {
                count += calculate(numStr, index + 1, nextStarted == 1 ? digit : 10, nextTight, nextStarted, k, memo);
            } else {
                if (Math.abs(digit - prev) <= k) {
                    count += calculate(numStr, index + 1, digit, nextTight, nextStarted, k, memo);
                }
            }
        }
        memo[index][prev][tight][started] = count;
        return count;
    }
}