// Leetcode 3213: Costruct String with Minimum Cost
// https://leetcode.com/problems/construct-string-with-minimum-cost/
// Solved on 27th of February, 2026
class Solution {
    /**
     * Calculates the minimum cost to construct the target string using a given set of words.
     *
     * @param target The string to be constructed.
     * @param words  An array of strings available for construction.
     * @param costs  An array of integers representing the cost of using each word.
     * @return The minimum cost to construct the target string, or -1 if it's impossible.
     */
    public int minimumCost(String target, String[] words, int[] costs) {
        int maxNodes = 50005;
        int[][] next = new int[maxNodes][26];
        int[] fail = new int[maxNodes];
        int[] dictLink = new int[maxNodes];
        int[] minCost = new int[maxNodes];
        int[] len = new int[maxNodes];
        
        for (int i = 0; i < maxNodes; i++) {
            minCost[i] = Integer.MAX_VALUE;
            dictLink[i] = -1;
        }
        
        int nodeCount = 1;
        for (int i = 0; i < words.length; i++) {
            String w = words[i];
            int c = costs[i];
            int curr = 0;
            for (int j = 0; j < w.length(); j++) {
                int charIdx = w.charAt(j) - 'a';
                if (next[curr][charIdx] == 0) {
                    next[curr][charIdx] = nodeCount++;
                }
                curr = next[curr][charIdx];
            }
            minCost[curr] = Math.min(minCost[curr], c);
            len[curr] = w.length();
        }
        
        int[] q = new int[maxNodes];
        int head = 0, tail = 0;
        
        for (int c = 0; c < 26; c++) {
            if (next[0][c] != 0) {
                fail[next[0][c]] = 0;
                q[tail++] = next[0][c];
            }
        }
        
        while (head < tail) {
            int u = q[head++];
            
            int f = fail[u];
            if (minCost[f] != Integer.MAX_VALUE) {
                dictLink[u] = f;
            } else {
                dictLink[u] = dictLink[f];
            }
            
            for (int c = 0; c < 26; c++) {
                if (next[u][c] != 0) {
                    fail[next[u][c]] = next[fail[u]][c];
                    q[tail++] = next[u][c];
                } else {
                    next[u][c] = next[fail[u]][c];
                }
            }
        }
        
        int n = target.length();
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            dp[i] = Integer.MAX_VALUE;
        }
        dp[0] = 0;
        
        int curr = 0;
        for (int i = 1; i <= n; i++) {
            curr = next[curr][target.charAt(i - 1) - 'a'];
            
            int temp = curr;
            if (minCost[temp] == Integer.MAX_VALUE) {
                temp = dictLink[temp];
            }
            while (temp != -1 && temp != 0) {
                if (dp[i - len[temp]] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[i - len[temp]] + minCost[temp]);
                }
                temp = dictLink[temp];
            }
        }
        
        return dp[n] == Integer.MAX_VALUE ? -1 : dp[n];
    }
}