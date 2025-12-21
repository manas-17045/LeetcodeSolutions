// Leetcode 3704: Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/
// Solved on 21st of December, 2025
class Solution {
    /**
     * Given an integer n, return the number of pairs of non-zero integers (a, b) such that a + b = n.
     * A non-zero integer is an integer that does not contain the digit 0.
     * @param n The target sum.
     * @return The number of non-zero pairs (a, b) that sum to n.
     */
    public long countNoZeroPairs(long n) {
        String s = String.valueOf(n);
        int len = s.length();
        int[] digits = new int[len];
        for (int i = 0; i < len; i++) {
            digits[i] = s.charAt(len - 1 - i) - '0';
        }

        long count = 0;
        for (int lenA = 1; lenA <= len; lenA++) {
            for (int lenB = 1; lenB <= len; lenB++) {
                count += solve(digits, lenA, lenB);
            }
        }
        return count;
    }

    private long solve(int[] digits, int lenA, int lenB) {
        long[] dp = new long[2];
        dp[0] = 1;

        for (int i = 0; i < digits.length; i++) {
            long[] nextDp = new long[2];
            int digit = digits[i];

            int minA = (i < lenA) ? 1 : 0;
            int maxA = (i < lenA) ? 9 : 0;
            int minB = (i < lenB) ? 1 : 0;
            int maxB = (i < lenB) ? 9 : 0;

            for (int carry = 0; carry <= 1; carry++) {
                if (dp[carry] == 0) {
                    continue;
                }

                for (int nextCarry = 0; nextCarry <= 1; nextCarry++) {
                    int targetSum = digit + nextCarry * 10 - carry;
                    int low = Math.max(minA, targetSum - maxB);
                    int high = Math.min(maxA, targetSum - minB);

                    if (low <= high) {
                        nextDp[nextCarry] += dp[carry] * (high - low + 1);
                    }
                }
            }
            dp = nextDp;
        }
        return dp[0];
    }
}