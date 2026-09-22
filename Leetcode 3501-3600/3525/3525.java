// Leetcode 3525: Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/
// Solved on 22nd of September, 2026
class Solution {
    private int[] totalProduct;
    private int[][] prefixCounts;
    private int kValue;

    /**
     * Computes the x-values for a given array of queries by updating elements 
     * and determining the frequency of specific prefix product remainders.
     *
     * @param nums    the original array of positive integers
     * @param k       the modulo operand for product calculations
     * @param queries the 2D array representing update and evaluation queries
     * @return an array of integers representing the results for each query
     */
    public int[] resultArray(int[] nums, int k, int[][] queries) {
        int n = nums.length;
        this.kValue = k;
        this.totalProduct = new int[4 * n];
        this.prefixCounts = new int[4 * n][k];
        
        buildTree(0, 0, n - 1, nums);
        
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int index = queries[i][0];
            int value = queries[i][1];
            int start = queries[i][2];
            int x = queries[i][3];
            
            updateTree(0, 0, n - 1, index, value);
            int[] queryResult = queryTree(0, 0, n - 1, start, n - 1);
            result[i] = queryResult[x];
        }
        
        return result;
    }

    private void buildTree(int node, int left, int right, int[] nums) {
        if (left == right) {
            totalProduct[node] = nums[left] % kValue;
            prefixCounts[node][nums[left] % kValue] = 1;
            return;
        }
        int mid = left + (right - left) / 2;
        buildTree(2 * node + 1, left, mid, nums);
        buildTree(2 * node + 2, mid + 1, right, nums);
        mergeNodes(node);
    }

    private void mergeNodes(int node) {
        int leftChild = 2 * node + 1;
        int rightChild = 2 * node + 2;
        
        totalProduct[node] = (totalProduct[leftChild] * totalProduct[rightChild]) % kValue;
        
        for (int i = 0; i < kValue; i++) {
            prefixCounts[node][i] = prefixCounts[leftChild][i];
        }
        
        for (int i = 0; i < kValue; i++) {
            if (prefixCounts[rightChild][i] > 0) {
                int newMod = (totalProduct[leftChild] * i) % kValue;
                prefixCounts[node][newMod] += prefixCounts[rightChild][i];
            }
        }
    }

    private void updateTree(int node, int left, int right, int index, int value) {
        if (left == right) {
            totalProduct[node] = value % kValue;
            for (int i = 0; i < kValue; i++) {
                prefixCounts[node][i] = 0;
            }
            prefixCounts[node][value % kValue] = 1;
            return;
        }
        int mid = left + (right - left) / 2;
        if (index <= mid) {
            updateTree(2 * node + 1, left, mid, index, value);
        } else {
            updateTree(2 * node + 2, mid + 1, right, index, value);
        }
        mergeNodes(node);
    }

    private int[] queryTree(int node, int left, int right, int queryLeft, int queryRight) {
        if (queryLeft <= left && right <= queryRight) {
            int[] res = new int[kValue + 1];
            res[kValue] = totalProduct[node];
            for (int i = 0; i < kValue; i++) {
                res[i] = prefixCounts[node][i];
            }
            return res;
        }
        
        int mid = left + (right - left) / 2;
        
        if (queryRight <= mid) {
            return queryTree(2 * node + 1, left, mid, queryLeft, queryRight);
        }
        if (queryLeft > mid) {
            return queryTree(2 * node + 2, mid + 1, right, queryLeft, queryRight);
        }
        
        int[] leftRes = queryTree(2 * node + 1, left, mid, queryLeft, queryRight);
        int[] rightRes = queryTree(2 * node + 2, mid + 1, right, queryLeft, queryRight);
        
        int[] mergedRes = new int[kValue + 1];
        mergedRes[kValue] = (leftRes[kValue] * rightRes[kValue]) % kValue;
        
        for (int i = 0; i < kValue; i++) {
            mergedRes[i] = leftRes[i];
        }
        
        for (int i = 0; i < kValue; i++) {
            if (rightRes[i] > 0) {
                int newMod = (leftRes[kValue] * i) % kValue;
                mergedRes[newMod] += rightRes[i];
            }
        }
        
        return mergedRes;
    }
}