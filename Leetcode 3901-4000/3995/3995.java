// Leetcode 3995: Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/
// Solved on 16th of August, 2026
class Solution {
    /**
     * Calculates the minimum cost to convert the source string to the target string.
     *
     * @param source The source string.
     * @param target The target string.
     * @param rules  The rules for converting the source string.
     * @param costs  The costs for the rules.
     * @return The minimum cost to convert the source string to the target string.
     */
    public int minCost(String source, String target, List<List<String>> rules, int[] costs) {
        int n = source.length();
        int m = rules.size();
        char[] src = source.toCharArray();
        char[] tgt = target.toCharArray();
        
        char[][] patterns = new char[m][];
        char[][] replacements = new char[m][];
        int[] trueCosts = new int[m];
        int[] ruleLengths = new int[m];
        
        for (int i = 0; i < m; i++) {
            String p = rules.get(i).get(0);
            String r = rules.get(i).get(1);
            patterns[i] = p.toCharArray();
            replacements[i] = r.toCharArray();
            ruleLengths[i] = p.length();
            
            int stars = 0;
            for (char c : patterns[i]) {
                if (c == '*') {
                    stars++;
                }
            }
            trueCosts[i] = costs[i] + stars;
        }
        
        long[] dp = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            dp[i] = Long.MAX_VALUE;
        }
        dp[0] = 0;
        
        for (int i = 0; i < n; i++) {
            if (dp[i] == Long.MAX_VALUE) {
                continue;
            }
            
            if (src[i] == tgt[i]) {
                if (dp[i] < dp[i + 1]) {
                    dp[i + 1] = dp[i];
                }
            }
            
            for (int k = 0; k < m; k++) {
                int len = ruleLengths[k];
                if (i + len <= n) {
                    boolean match = true;
                    for (int j = 0; j < len; j++) {
                        if (replacements[k][j] != tgt[i + j] || 
                            (patterns[k][j] != '*' && patterns[k][j] != src[i + j])) {
                            match = false;
                            break;
                        }
                    }
                    if (match) {
                        long nextCost = dp[i] + trueCosts[k];
                        if (nextCost < dp[i + len]) {
                            dp[i + len] = nextCost;
                        }
                    }
                }
            }
        }
        
        if (dp[n] == Long.MAX_VALUE) {
            return -1;
        }
        
        return (int) dp[n];
    }
}