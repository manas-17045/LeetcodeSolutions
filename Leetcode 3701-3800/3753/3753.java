// Leetcode 3753: Total Waviness of Numbers in Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/
// Solved on 21st of December, 2025
import java.util.Arrays;

class Solution {
    private String s;
    private long[][][][][][] memo;

    /**
     * Calculates the total waviness of numbers within a given range [num1, num2].
     * @param num1 The lower bound of the range (inclusive).
     * @param num2 The upper bound of the range (inclusive).
     * @return The total waviness of all numbers in the range.
     */
    public long totalWaviness(long num1, long num2) {
        return solve(num2) - solve(num1 - 1);
    }

    private long solve(long num) {
        if (num < 0) {
            return 0;
        }
        if (num == 0) {
            return 0;
        }
        s = String.valueOf(num);
        int n = s.length();
        
        memo = new long[n][2][11][11][2][2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 11; k++) {
                    for (int l = 0; l < 11; l++) {
                        for (int m = 0; m < 2; m++) {
                            Arrays.fill(memo[i][j][k][l][m], -1);
                        }
                    }
                }
            }
        }
        return dp(0, 1, 10, 10, 1)[1];
    }

    private long[] dp(int idx, int tight, int last, int secondLast, int leading) {
        if (idx == s.length()) {
            return new long[]{1, 0};
        }
        if (memo[idx][tight][last][secondLast][leading][0] != -1) {
            return memo[idx][tight][last][secondLast][leading];
        }

        long count = 0;
        long waviness = 0;
        int limit = (tight == 1) ? (s.charAt(idx) - '0') : 9;

        for (int d = 0; d <= limit; d++) {
            int nextTight = (tight == 1 && d == limit) ? 1 : 0;
            int nextLeading = (leading == 1 && d == 0) ? 1 : 0;
            int nextLast = (nextLeading == 1) ? 10 : d;
            int nextSecondLast = (nextLeading == 1) ? 10 : last;

            int isPeakOrValley = 0;
            if (leading == 0 && secondLast != 10) {
                if (last > secondLast && last > d) {
                    isPeakOrValley = 1;
                } else if (last < secondLast && last < d) {
                    isPeakOrValley = 1;
                }
            }

            long[] res = dp(idx + 1, nextTight, nextLast, nextSecondLast, nextLeading);
            
            count += res[0];
            iwaviness += res[1] + (res[0] * isPeakOrValley);
        }

        return memo[idx][tight][last][secondLast][leading] = new long[]{count, waviness};
    }
}