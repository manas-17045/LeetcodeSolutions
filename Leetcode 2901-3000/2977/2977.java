// Leetcode 2977: Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/
// Solved on 30th of January, 2026
import java.util.Arrays;

class Solution {
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        int id = -1;
    }

    /**
     * Calculates the minimum cost to convert the source string to the target string
     * using a set of allowed substring conversions with associated costs.
     *
     * @param source   The initial string to be converted.
     * @param target   The target string to reach.
     * @param original An array of strings that can be replaced.
     * @param changed  An array of strings that can replace the corresponding strings in original.
     * @param cost     An array of costs associated with each conversion from original[i] to changed[i].
     * @return The minimum cost to convert source to target, or -1 if conversion is impossible.
     */
    public long minimumCost(String source, String target, String[] original, String[] changed, int[] cost) {
        int n = source.length();
        int m = original.length;
        
        TrieNode root = new TrieNode();
        int nodeCount = 0;

        for (String s : original) {
            TrieNode node = root;
            for (char c : s.toCharArray()) {
                if (node.children[c - 'a'] == null) {
                    node.children[c - 'a'] = new TrieNode();
                }
                node = node.children[c - 'a'];
            }
            if (node.id == -1) {
                node.id = nodeCount++;
            }
        }

        for (String s : changed) {
            TrieNode node = root;
            for (char c : s.toCharArray()) {
                if (node.children[c - 'a'] == null) {
                    node.children[c - 'a'] = new TrieNode();
                }
                node = node.children[c - 'a'];
            }
            if (node.id == -1) {
                node.id = nodeCount++;
            }
        }

        long[][] dist = new long[nodeCount][nodeCount];
        for (long[] row : dist) {
            Arrays.fill(row, Long.MAX_VALUE / 2);
        }
        for (int i = 0; i < nodeCount; i++) {
            dist[i][i] = 0;
        }

        for (int i = 0; i < m; i++) {
            int u = getId(root, original[i]);
            int v = getId(root, changed[i]);
            dist[u][v] = Math.min(dist[u][v], cost[i]);
        }

        for (int k = 0; k < nodeCount; k++) {
            for (int i = 0; i < nodeCount; i++) {
                if (dist[i][k] >= Long.MAX_VALUE / 2) continue;
                for (int j = 0; j < nodeCount; j++) {
                    if (dist[k][j] >= Long.MAX_VALUE / 2) continue;
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        long[] dp = new long[n + 1];
        Arrays.fill(dp, Long.MAX_VALUE / 2);
        dp[n] = 0;

        for (int i = n - 1; i >= 0; i--) {
            if (source.charAt(i) == target.charAt(i)) {
                dp[i] = Math.min(dp[i], dp[i + 1]);
            }

            TrieNode p1 = root;
            TrieNode p2 = root;

            for (int j = i; j < n; j++) {
                int c1 = source.charAt(j) - 'a';
                int c2 = target.charAt(j) - 'a';

                if (p1.children[c1] == null || p2.children[c2] == null) {
                    break;
                }

                p1 = p1.children[c1];
                p2 = p2.children[c2];

                if (p1.id != -1 && p2.id != -1) {
                    if (dist[p1.id][p2.id] < Long.MAX_VALUE / 2) {
                        dp[i] = Math.min(dp[i], dist[p1.id][p2.id] + dp[j + 1]);
                    }
                }
            }
        }

        return dp[0] >= Long.MAX_VALUE / 2 ? -1 : dp[0];
    }

    private int getId(TrieNode root, String s) {
        TrieNode node = root;
        for (char c : s.toCharArray()) {
            node = node.children[c - 'a'];
        }
        return node.id;
    }
}