// Leetcode 3534: Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/
// Solved on 10th of July, 2026
class Solution {
    /**
     * Given three integers n, maxDiff and an array nums of length n. 
     * We define a graph as follows:
     * - There are n nodes labeled from 0 to n - 1.
     * - An edge can be formed between node i and node j (0 <= i, j < n)
     *   if and only if nums[i] + nums[j] <= maxDiff.
     * 
     * Return an array answering the following queries: for each query 
     * where queries[i] = [ui, vi], check if there exists a path from ui to vi.
     * 
     * @param n Number of nodes in the graph.
     * @param nums Array of integers.
     * @param maxDiff Maximum allowed difference between adjacent node values.
     * @param queries Array of queries, where each query is a pair of node indices.
     * @return Array of integers, where each element is the minimum number of edges 
     * required to travel from the first node to the second node in a query, 
     * or -1 if no path exists.
     */
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        long[] packed = new long[n];
        for (int i = 0; i < n; i++) {
            packed[i] = ((long) nums[i] << 32) | i;
        }
        java.util.Arrays.sort(packed);

        int[] pos = new int[n];
        int[] sortedVals = new int[n];
        for (int i = 0; i < n; i++) {
            sortedVals[i] = (int) (packed[i] >> 32);
            pos[(int) (packed[i] & 0xFFFFFFFFL)] = i;
        }

        int[][] up = new int[n][18];
        int right = 0;
        for (int left = 0; left < n; left++) {
            while (right + 1 < n && sortedVals[right + 1] - sortedVals[left] <= maxDiff) {
                right++;
            }
            up[left][0] = right;
        }

        for (int j = 1; j < 18; j++) {
            for (int i = 0; i < n; i++) {
                up[i][j] = up[up[i][j - 1]][j - 1];
            }
        }

        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int p1 = pos[queries[i][0]];
            int p2 = pos[queries[i][1]];

            if (p1 == p2) {
                answer[i] = 0;
                continue;
            }

            if (p1 > p2) {
                int temp = p1;
                p1 = p2;
                p2 = temp;
            }

            if (up[p1][17] < p2) {
                answer[i] = -1;
                continue;
            }

            int curr = p1;
            int jumps = 0;
            for (int j = 17; j >= 0; j--) {
                if (up[curr][j] < p2) {
                    curr = up[curr][j];
                    jumps += (1 << j);
                }
            }
            answer[i] = jumps + 1;
        }

        return answer;
    }
}