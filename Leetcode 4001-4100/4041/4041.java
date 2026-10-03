// Leetcode 4041: Minimum Operations to Form Subset Sum II
// https://leetcode.com/problems/minimum-operations-to-form-subset-sum-ii/ 
// Solved on 3rd of October, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum number of operations required so that some subset of the resulting array
     * has a sum exactly equal to the specified target sum. An operation consists of either multiplying
     * an element by 2 or dividing it by 2 (taking the floor).
     *
     * @param nums the input array of integers
     * @param sum the target subset sum to achieve
     * @return the minimum number of operations needed, or -1 if it is impossible to form the sum
     */
    public int minOperations(int[] nums, int sum) {
        int[] dp = new int[sum + 1];
        Arrays.fill(dp, 1000000);
        dp[0] = 0;

        int[] itemCost = new int[sum + 1];
        Arrays.fill(itemCost, 1000000);
        int[] reach = new int[500];

        for (int x : nums) {
            int count = 0;
            int val = x;
            int div = 0;

            while (true) {
                int cur = val;
                int mul = 0;

                while (cur <= sum) {
                    if (cur > 0 && itemCost[cur] == 1000000) {
                        reach[count++] = cur;
                    }
                    if (cur > 0) {
                        int cost = div + mul;
                        if (cost < itemCost[cur]) {
                            itemCost[cur] = cost;
                        }
                    }
                    if (cur == 0) {
                        break;
                    }
                    cur *= 2;
                    mul++;
                }

                if (val == 0) {
                    break;
                }
                val /= 2;
                div++;
            }

            for (int s = sum; s >= 0; s--) {
                if (dp[s] != 1000000) {
                    int currentDpS = dp[s];
                    for (int i = 0; i < count; i++) {
                        int v = reach[i];
                        int newS = s + v;
                        if (newS <= sum) {
                            int totalCost = currentDpS + itemCost[v];
                            if (totalCost < dp[newS]) {
                                dp[newS] = totalCost;
                            }
                        }
                    }
                }
            }

            for (int i = 0; i < count; i++) {
                itemCost[reach[i]] = 1000000;
            }
        }

        if (dp[sum] == 1000000) {
            return -1;
        }
        return dp[sum];
    }
}