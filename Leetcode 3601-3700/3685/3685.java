// Leetcode 3685: Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/
// Solved on 22nd of November, 2025
class Solution {
    /**
     * Determines for each possible cap value `x` (from 1 to n) if there exists a subsequence
     * whose sum is at most `k` after capping all its elements at `x`.
     * @param nums The input array of integers.
     * @param k The maximum allowed sum.
     * @return A boolean array where `answer[x-1]` is true if such a subsequence exists for cap `x`.
     */
    public boolean [] subsequenceSumAfterCapping(int[] nums, int k) {
        int n = nums.length;
        int[] freq = new int[n + 1];
        for (int num : nums) {
            freq[num]++;
        }

        boolean[] dp = new boolean[k + 1];
        dp[0] = true;

        boolean[] answer = new boolean[n];
        int remaining = n;

        for (int x = 1; x <= n; x++) {
            boolean possible = false;
            for (int s = k; s >= 0; s -= x) {
                if (dp[s]) {
                    int needed = (k - s) / x;
                    if (needed <= remaining) {
                        possible = true;
                        break;
                    }
                }
            }
            answer[x - 1] = possible;

            int count = freq[x];
            if (count > 0) {
                for (int i = 0; i < count; i++) {
                    for (int j = k; j >= x; j--) {
                        if (!dp[j] && dp[j - x]) {
                            dp[j] = true;
                        }
                    }
                }
            }
            remaining -= count;
        }

        return answer;
    }
}