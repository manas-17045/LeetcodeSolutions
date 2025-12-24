// Leetcode 3784: Minimum Deletion Cost to make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/
// Solved on 24th of December, 2025
class Solution {
    /**
     * Calculates the minimum deletion cost to make all characters in the string equal.
     * @param s The input string.
     * @param cost An array where cost[i] is the cost to delete the i-th character.
     * @return The minimum deletion cost.
     */
    public long minCost(String s,int[] cost) {
        long totalSum = 0;
        long[] charSums = new long[26];
        int n = s.length();

        for (int i = 0; i < n; i++) {
            int val = cost[i];
            totalSum += val;
            charSums[s.charAt(i) - 'a'] += val;
        }

        long maxKept = 0;
        for (long sum : charSums) {
            maxKept = Math.max(maxKept, sum);
        }

        return totalSum - maxKept;
    }
}