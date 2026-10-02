// Leetcode 4040: Minimum Operations to Form Subset Sum I
// https://leetcode.com/problems/minimum-operations-to-form-subset-sum-i/
// Solved on 2nd of October, 2026
import java.util.Arrays;

class Solution {
    /**
     * Finds the minimum total operations needed to transform a subset of elements
     * such that their sum equals the target sum using valid multiplications or divisions.
     *
     * @param nums the array of positive integers to select and transform
     * @param sum the exact target subset sum to achieve
     * @return the minimum operations required, or -1 if the target sum cannot be formed
     */
    public int minOperations(int[] nums, int sum) {
        int inf = 1_000_000_000;
        int[] dp = new int[sum + 1];
        Arrays.fill(dp, inf);
        dp[0] = 0;

        int[] valChoices = new int[64];
        int[] costChoices = new int[64];
        int maxReach = 0;

        for (int num : nums) {
            int choiceCount = 0;
            int maxChoiceVal = 0;

            if (num <= sum) {
                valChoices[choiceCount] = num;
                costChoices[choiceCount] = 0;
                choiceCount++;
                maxChoiceVal = Math.max(maxChoiceVal, num);
            }

            int divVal = num / 2;
            int divOps = 1;
            while (divVal > 0) {
                if (divVal <= sum) {
                    valChoices[choiceCount] = divVal;
                    costChoices[choiceCount] = divOps;
                    choiceCount++;
                    maxChoiceVal = Math.max(maxChoiceVal, divVal);
                }
                divVal /= 2;
                divOps++;
            }

            long mulVal = (long) num * 2;
            int mulOps = 1;
            while (mulVal <= sum) {
                valChoices[choiceCount] = (int) mulVal;
                costChoices[choiceCount] = mulOps;
                choiceCount++;
                maxChoiceVal = Math.max(maxChoiceVal, (int) mulVal);
                mulVal *= 2;
                mulOps++;
            }

            if (choiceCount == 0) {
                continue;
            }

            int newMaxReach = Math.min(sum, maxReach + maxChoiceVal);
            for (int s = newMaxReach; s >= 1; s--) {
                for (int i = 0; i < choiceCount; i++) {
                    int v = valChoices[i];
                    int c = costChoices[i];
                    if (s >= v && dp[s - v] != inf) {
                        dp[s] = Math.min(dp[s], dp[s - v] + c);
                    }
                }
            }
            maxReach = newMaxReach;

            if (dp[sum] == 0) {
                return 0;
            }
        }

        return dp[sum] == inf ? -1 : dp[sum];
    }
}