// Leetcode 2916: Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/
// Solved on 16th of October, 2026
class Solution {

    private long[] treeSum;
    private long[] treeSqSum;
    private long[] treeLazy;
    private long modVal = 1000000007;

    /**
     * Calculates the sum of the squares of distinct counts of all subarrays.
     *
     * @param nums the input array of integers
     * @return the total sum of squares of distinct counts modulo 10^9 + 7
     */
    public int sumCounts(int[] nums) {
        int n = nums.length;
        treeSum = new long[4 * n];
        treeSqSum = new long[4 * n];
        treeLazy = new long[4 * n];
        
        int[] lastSeen = new int[100005];
        for (int i = 0; i < lastSeen.length; i++) {
            lastSeen[i] = -1;
        }

        long totalSum = 0;
        for (int i = 0; i < n; i++) {
            int startIdx = lastSeen[nums[i]] + 1;
            updateTree(1, 0, n - 1, startIdx, i, 1);
            lastSeen[nums[i]] = i;
            totalSum = (totalSum + treeSqSum[1]) % modVal;
        }
        
        return (int) totalSum;
    }

    private void applyLazy(int node, int start, int end, long val) {
        long len = end - start + 1;
        long valMod = val % modVal;
        long sumMod = treeSum[node];
        long sqSumMod = treeSqSum[node];

        long termOne = (2 * valMod * sumMod) % modVal;
        long termTwo = (valMod * valMod % modVal) * len % modVal;

        treeSqSum[node] = (sqSumMod + termOne + termTwo) % modVal;
        treeSum[node] = (sumMod + valMod * len) % modVal;
        treeLazy[node] = (treeLazy[node] + valMod) % modVal;
    }

    private void pushDown(int node, int start, int end) {
        if (treeLazy[node] != 0) {
            int mid = start + (end - start) / 2;
            applyLazy(2 * node, start, mid, treeLazy[node]);
            applyLazy(2 * node + 1, mid + 1, end, treeLazy[node]);
            treeLazy[node] = 0;
        }
    }

    private void updateTree(int node, int start, int end, int left, int right, long val) {
        if (left > end || right < start) {
            return;
        }
        
        if (left <= start && end <= right) {
            applyLazy(node, start, end, val);
            return;
        }
        
        pushDown(node, start, end);
        int mid = start + (end - start) / 2;
        
        updateTree(2 * node, start, mid, left, right, val);
        updateTree(2 * node + 1, mid + 1, end, left, right, val);
        
        treeSum[node] = (treeSum[2 * node] + treeSum[2 * node + 1]) % modVal;
        treeSqSum[node] = (treeSqSum[2 * node] + treeSqSum[2 * node + 1]) % modVal;
    }
}