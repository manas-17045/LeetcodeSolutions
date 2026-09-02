// Leetcode 3743: Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/
// Solved on 2nd of September, 2026
class Solution {
    /**
     * Calculates the maximum possible score among all cyclic partitions of the array
     * into at most k subarrays.
     *
     * @param nums the cyclic array of integers
     * @param k the maximum number of subarrays allowed in the partition
     * @return the maximum partition score achievable
     */
    public long maximumScore(int[] nums, int k) {
        int n = nums.length;
        int maxPicks = Math.min(2 * k, n);
        long negInf = -1_000_000_000_000_000_000L;
        long maxScore = 0;

        for (int startBalance = 0; startBalance <= 2; startBalance++) {
            long[][] dp = new long[maxPicks + 1][3];
            for (int p = 0; p <= maxPicks; p++) {
                dp[p][0] = negInf;
                dp[p][1] = negInf;
                dp[p][2] = negInf;
            }
            dp[0][startBalance] = 0;

            int currPicks = 0;
            for (int num : nums) {
                int limit = Math.min(currPicks, maxPicks - 1);
                for (int p = limit; p >= 0; p--) {
                    for (int bal = 0; bal <= 2; bal++) {
                        long currentVal = dp[p][bal];
                        if (currentVal <= negInf / 2) {
                            continue;
                        }
                        if (bal + 1 <= 2) {
                            if (currentVal + num > dp[p + 1][bal + 1]) {
                                dp[p + 1][bal + 1] = currentVal + num;
                            }
                        }
                        if (bal - 1 >= 0) {
                            if (currentVal - num > dp[p + 1][bal - 1]) {
                                dp[p + 1][bal - 1] = currentVal - num;
                            }
                        }
                    }
                }
                currPicks = Math.min(maxPicks, currPicks + 1);
            }

            for (int p = 0; p <= maxPicks; p += 2) {
                if (dp[p][startBalance] > maxScore) {
                    maxScore = dp[p][startBalance];
                }
            }
        }

        return maxScore;
    }
}