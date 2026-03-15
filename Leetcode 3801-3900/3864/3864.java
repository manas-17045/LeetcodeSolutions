// Leetcode 3864: Minimum Cost to Partition a Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/
// Solved on 15th of March, 2026
class Solution {
    /**
     * Calculates the minimum cost to partition a binary string based on encoding and flat costs.
     *
     * @param s        The binary string to be partitioned.
     * @param encCost  The cost multiplier for encoded segments.
     * @param flatCost The fixed cost for segments containing only zeros.
     * @return         The minimum total cost to partition the string.
     */
    public long minCost(String s, int encCost, int flatCost) {
        int n = s.length();
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + (s.charAt(i) - '0');
        }
        return solve(0, n - 1, pref, encCost, flatCost);
    }

    private long solve(int l, int r, int[] pref, int encCost, int flatCost) {
        long len = r - l + 1;
        long x = pref[r + 1] - pref[l];
        long cost = x == 0? flatCost : len * x * encCost;
        if (len % 2 == 0) {
            int mid = l + (int) (len / 2) - 1;
            long splitCost = solve(l, mid, pref, encCost, flatCost) + solve(mid + 1, r, pref, encCost, flatCost);
            if (splitCost < cost) {
                cost = splitCost;
            }
        }
        return cost;
    }
}