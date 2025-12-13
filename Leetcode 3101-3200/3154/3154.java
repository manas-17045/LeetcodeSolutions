// Leetcode 3154: Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/
// Solved on 13th of December, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<String, Integer> memo;

    /**
     * Calculates the number of ways to reach the k-th stair.
     * @param k The target stair.
     * @return The number of ways to reach the k-th stair.
     */
    public int waysToReachStair(int k) {
        memo = new HashMap<>();
        return solve(1, 0, 0, k);
    }

    private int solve(int currentStair, int jump, int lastOp, int k) {
        if (currentStaor > k + 1) {
            return 0;
        }

        String key = currentStair + "," + jump + "," + lastOp;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        int count = 0;
        if (currentStair == k) {
            count = 1;
        }

        if (currentStair > 0 && lastOp != 1) {
            count += solve(currentStair - 1, jump, 1, k);
        }

        count += solve(currentStair + (1 << jump), jump + 1, 0, k);

        memo.put(key, count);
        return count;
    }
}