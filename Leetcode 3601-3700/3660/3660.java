// Leetcode 3660: Jump Game IX
// https://leetcode.com/problems/jump-game-ix/
// Solved on 28th of December, 2025
import java.util.*;

class Solution {
    /**
     * Given an array of integers nums, return an array ans of the same length where ans[i] is the maximum value
     * that can be obtained by starting at index i and making a sequence of jumps.
     * @param nums The input array of integers.
     * @return An array ans where ans[i] is the maximum value obtainable from index i.
     */
    public int[] maxValue(int[] nums) {
        int n = nums.length;
        List<Integer> pIndices = new ArrayList<>();
        int currentMax = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] > currentMax) {
                pIndices.add(i);
                currentMax = nums[i];
            }
        }

        int m = pIndices.size();
        int[] mValues = new int[m];
        int[] pVals = new int[m];

        for (int k = 0; k < m; k++) {
            int start = pIndices.get(k);
            int end = (k == m - 1) ? n : pIndices.get(k + 1);
            int minVal = Integer.MAX_VALUE;
            for (int i = start; i < end; i++) {
                minVal = Math.min(minVal, nums[i]);
            }
            mValues[k] = minVal;
            pVals[k] = nums[start];
        }

        TreeSet<Integer> sortedValues = new TreeSet<>();
        for (int v : mValues) {
            sortedValues.add(v);
        }
        for (int v : pVals) {
            sortedValues.add(v);
        }

        Map<Integer, Integer> rankMap = new HashMap<>();
        int rank = 1;
        for (int v : sortedValues) {
            rankMap.put(v, rank++);
        }

        int[] ansP = new int[m];
        int[] bit = new int[rank + 1];

        for (int k = m - 1; k >= 0; k--) {
            int currentVal = pVals[k];
            int r = rankMap.get(currentVal);
            int bestFuture = query(bit, r - 1);
            ansP[k] = Math.max(currentVal, bestFuture);
            
            int mRank = rankMap.get(mValues[k]);
            update(bit, mRank, ansP[k]);
        }

        int[] ans = new int[n];
        for (int k = 0; k < m; k++) {
            int start = pIndices.get(k);
            int end = (k == m - 1) ? n : pIndices.get(k + 1);
            for (int i = start; i < end; i++) {
                ans[i] = ansP[k];
            }
        }

        return ans;
    }

    private void update(int[] bit, int idx, int val) {
        while (idx < bit.length) {
            bit[idx] = Math.max(bit[idx], val);
            idx += idx & -idx;
        }
    }

    private int query(int[] bit, int idx) {
        int res = 0;
        while (idx > 0) {
            res = Math.max(res, bit[idx]);
            idx -= idx & -idx;
        }
        return res;
    }
}