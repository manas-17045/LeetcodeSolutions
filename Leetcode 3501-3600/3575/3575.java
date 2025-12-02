// Leetcode 3575: Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/
// Solved on 2nd of November, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private long totalScore;
    private final int MOD = 1000000007;

    /**
     * Calculates the maximum good subtree score.
     * @param vals An array of integer values for each node.
     * @param par An array representing the parent of each node. par[i] is the parent of node i, or -1 if i is the root.
     * @return The total maximum good subtree score modulo 1000000007.
     */
    public int goodSubtreeSum(int[] vals, int[] par) {
        int n = vals.length;
        List<List<Integer>> children = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            children.add(new ArrayList<>());
        }

        for (int i = 0; i < n; i++) {
            if (par[i] != -1) {
                children.get(par[i]).add(i);
            }
        }

        totalScore = 0;
        dfs(0, children, vals);
        return (int) totalScore;
    }

    private long[] dfs(int node, List<List<Integer>> children, int[] vals) {
        long[] dp = new long[1024];
        Arrays.fill(dp, -1);
        dp[0] = 0;

        int nodeMask = getMask(vals[node]);
        if (nodeMask != -1) {
            dp[nodeMask] = vals[node];
        }

        for (int child : children.get(node)) {
            long[] childDp = dfs(child, children, vals);
            long[] nextDp = Arrays.copyOf(dp, 1024);

            int[] validMasksNode = new int[1024];
            int countNode = 0;
            for (int i = 0; i < 1024; i++) {
                if (dp[i] != -1) {
                    validMasksNode[countNode++] = i;
                }
            }

            int[] validMasksChild = new int[1024];
            int countChild = 0;
            for (int i = 0; i < 1024; i++) {
                if (childDp[i] != -1) {
                    validMasksChild[countChild++] = i;
                }
            }

            for (int i = 0; i < countNode; i++) {
                int mask1 = validMasksNode[i];
                long val1 = dp[mask1];
                
                for (int j = 0; j < countChild; j++) {
                    int mask2 = validMasksChild[j];
                    
                    if ((mask1 & mask2) == 0) {
                        int combinedMask = mask1 | mask2;
                        long combinedVal = val1 + childDp[mask2];
                        if (combinedVal > nextDp[combinedMask]) {
                            nextDp[combinedMask] = combinedVal;
                        }
                    }
                }
            }
            dp = nextDp;
        }

        long maxInSubtree = 0;
        for (long val : dp) {
            if (val > maxInSubtree) {
                maxInSubtree = val;
            }
        }
        totalScore = (totalScore + maxInSubtree) % MOD;

        return dp;
    }

    private int getMask(int val) {
        int mask = 0;
        if (val == 0) return 1;
        while (val > 0) {
            int digit = val % 10;
            if ((mask & (1 << digit)) != 0) {
                return -1;
            }
            mask |= (1 << digit);
            val /= 10;
        }
        return mask;
    }
}