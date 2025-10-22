// Leetcode 1569: Number of Ways to Reorder Array to Get Same BST
// https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
// Solved on 22nd of October, 2025
class Solution {
    private static final long MOD = 1_000_000_007L;
    private long[][] comb; // Pascal triangle for nCr

    /**
     * Calculates the number of ways to reorder an array `nums` such that the resulting Binary Search Tree (BST)
     * is structurally identical to the BST formed by inserting elements of `nums` in their original order.
     * @param nums The input array of integers.
     * @return The number of ways to reorder the array to get the same BST, modulo 1,000,000,007.
     */
    public int numOfWays(int[] nums) {
        int n = nums.length;
        // Build Pascal's triangle up to n
        comb = new long[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            comb[i][0] = comb[i][i] = 1;
            for (int j = 1; j < i; j++) {
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
            }
        }

        // Convert input to a list for easy splitting while preserving insertion order
        List<Integer> arr = new ArrayList<>(n);
        for (int v : nums) arr.add(v);

        long totalWays = dfs(arr);
        // Exclude the original ordering
        totalWays = (totalWays - 1 + MOD) % MOD;
        return (int) totalWays;
    }

    // Recursively compute number of ways for the sequence (first element is root)
    private long dfs(List<Integer> seq) {
        int size = seq.size();
        if (size <= 2) return 1L; // 0/1/2 nodes have only one BST-structure-preserving ordering

        int root = seq.get(0);
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        for (int i = 1; i < size; i++) {
            int v = seq.get(i);
            if (v < root) left.add(v);
            else right.add(v);
        }

        long leftWays = dfs(left);
        long rightWays = dfs(right);

        int l = left.size();
        int r = right.size();
        long interleaveWays = comb[l + r][l]; // ways to choose positions for left nodes among children

        return (((interleaveWays * leftWays) % MOD) * rightWays) % MOD;
    }
}