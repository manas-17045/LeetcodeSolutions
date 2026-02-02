// Leetcode 3013: Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
// Solved on 2nd of February, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum cost to divide an array into k subarrays with a distance constraint.
     *
     * @param nums The input integer array.
     * @param k    The number of subarrays to divide into.
     * @param dist The maximum distance allowed between the start of the second and last subarray.
     * @return The minimum total cost of the first elements of the k subarrays.
     */
    public long minimumCost(int[] nums, int k, int dist) {
        int n = nums.length;
        int target = k - 1;
        int[] sorted = new int[n - 1];
        System.arraycopy(nums, 1, sorted, 0, n - 1);
        Arrays.sort(sorted);
        
        int m = 0;
        for (int i = 0; i < sorted.length; i++) {
            if (i == 0 || sorted[i] != sorted[i - 1]) {
                sorted[m++] = sorted[i];
            }
        }
        
        int[] treeCnt = new int[m + 1];
        long[] treeSum = new long[m + 1];
        long minSum = Long.MAX_VALUE;
        
        for (int i = 1; i < n; i++) {
            int rank = Arrays.binarySearch(sorted, 0, m, nums[i]) + 1;
            update(treeCnt, treeSum, rank, 1, nums[i]);
            
            if (i > dist + 1) {
                int outVal = nums[i - dist - 1];
                int outRank = Arrays.binarySearch(sorted, 0, m, outVal) + 1;
                update(treeCnt, treeSum, outRank, -1, outVal);
            }
            
            if (i >= target) {
                minSum = Math.min(minSum, query(treeCnt, treeSum, target, sorted));
            }
        }
        
        return minSum + nums[0];
    }

    private void update(int[] treeCnt, long[] treeSum, int idx, int delta, int val) {
        long deltaSum = (long) val * delta;
        for (; idx < treeCnt.length; idx += idx & -idx) {
            treeCnt[idx] += delta;
            treeSum[idx] += deltaSum;
        }
    }

    private long query(int[] treeCnt, long[] treeSum, int k, int[] sorted) {
        int idx = 0;
        int currentCnt = 0;
        int maxBit = Integer.highestOneBit(treeCnt.length);
        
        for (int bit = maxBit; bit > 0; bit >>= 1) {
            int nextIdx = idx + bit;
            if (nextIdx < treeCnt.length && currentCnt + treeCnt[nextIdx] < k) {
                idx = nextIdx;
                currentCnt += treeCnt[idx];
            }
        }
        
        int targetRank = idx + 1;
        long sum = 0;
        int cnt = 0;
        int x = targetRank;
        while (x > 0) {
            sum += treeSum[x];
            cnt += treeCnt[x];
            x -= x & -x;
        }
        
        if (cnt > k) {
            sum -= (long) (cnt - k) * sorted[targetRank - 1];
        }
        
        return sum;
    }
}