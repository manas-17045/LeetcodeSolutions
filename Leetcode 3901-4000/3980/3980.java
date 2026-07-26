// Leetcode 3980: Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/
// Solved on 26th of July, 2026
class Solution {
    /**
     * Finds the minimum number of operations to transform s1 to s2.
     * @param s1 The source binary string.
     * @param s2 The target binary string.
     * @return The minimum number of operations to transform s1 to s2.
     */
    public int minOperations(String s1, String s2) {
        int n = s1.length();
        long dp0 = 0;
        long dp1 = (long) 1e9;

        for (int i = 0; i < n; i++) {
            long nextDp0 = (long) 1e9;
            long nextDp1 = (long) 1e9;

            for (int carried = 0; carried <= 1; carried++) {
                long currentCost = (carried == 0) ? dp0 : dp1;
                if (currentCost >= 1e9) {
                    continue;
                }

                char curVal = (carried == 1) ? '0' : s1.charAt(i);

                if (curVal == s2.charAt(i)) {
                    nextDp0 = Math.min(nextDp0, currentCost);
                } else if (curVal == '0' && s2.charAt(i) == '1') {
                    nextDp0 = Math.min(nextDp0, currentCost + 1);
                }

                if (i < n - 1) {
                    int opCost = 1;
                    opCost += (curVal == '0') ? 1 : 0;
                    opCost += (s1.charAt(i + 1) == '0') ? 1 : 0;
                    opCost += (s2.charAt(i) == '1') ? 1 : 0;

                    nextDp1 = Math.min(nextDp1, currentCost + opCost);
                }
            }

            dp0 = nextDp0;
            dp1 = nextDp1;
        }

        return dp0 >= 1e9 ? -1 : (int) dp0;
    }
}