// Leetcode 3751: Total Waviness of Numbers in Range I
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/
// Solved on 25th of December, 2025
import java.util.Arrays;

class Solution {
    private long[][][][][] memo;
    private char[] s;

    /**
     * Calculates the total "waviness" of numbers within a given range [num1, num2].
     * A number's waviness is determined by the alternating pattern of its digits.
     * @param num1 The lower bound of the range (inclusive).
     * @param num2 The upper bound of the range (inclusive).
     * @return The total waviness of numbers in the range.
     */
    public int totalWaviness(int num1, int num2) {
        return solve(num2) - solve(num1 - 1);
    }

    private int solve(int num) {
        if (num < 100) {
            return 0;
        }
        String str = String.valueOf(num);
        s = str.toCharArray();
        int n = s.length;
        memo = new long[n][11][11][2][2];
        for (long[][][][] a : memo) {
            for (long[][][] b : a) {
                for (long[][] c : b) {
                    for (long[] d : c) {
                        Arrays.fill(d, -1);
                    }
                }
            }
        }
        return (int) (dp(0, 10, 10, 1, 0) >> 32);
    }

    private long dp(int idx, int prev, int pprev, int isLimit, int isStarted) {
        if (idx == s.length) {
            return 1L;
        }
        if (memo[idx][prev][pprev][isLimit][isStarted] != -1) {
            return memo[idx][prev][pprev][isLimit][isStarted];
        }

        long res = 0;
        int bound = (isLimit == 1) ? (s[idx] - '0') : 9;

        for (int digit = 0; digit <= bound; digit++) {
            int newLimit = (isLimit == 1 && digit == bound) ? 1 : 0;
            int newStarted = (isStarted == 1 || digit > 0) ? 1 : 0;
            int newPrev = (newStarted == 0) ? 10 : digit;
            int newPprev = (newStarted == 0) ? 10 : ((isStarted == 0) ? 10 : prev);

            long subRes = dp(idx + 1, newPrev, newPprev, newLimit, newStarted);
            long count = subRes & 0xFFFFFFFFL;
            long waviness = subRes >> 32;

            if (isStarted == 1 && pprev != 10) {
                if ((prev > pprev && prev > digit) || (prev < pprev && prev < digit)) {
                    waviness += count;
                }
            }

            long totalCount = (res & 0xFFFFFFFFL) + count;
            long totalWaviness = (res >> 32) + waviness;
            res = (totalWaviness << 32) | totalCount;
        }

        return memo[idx][prev][pprev][isLimit][isStarted] = res;
    }
}