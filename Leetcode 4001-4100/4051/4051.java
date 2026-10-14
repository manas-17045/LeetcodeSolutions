// Leetcode 4051: Count Subarrays with Distant Sums
// https://leetcode.com/problems/count-subarrays-with-distant-sums/
// Solved on 14th of October, 2026
class Solution {
    /**
     * Calculates the total number of distant subarrays in the given array.
     * A subarray is considered distant if the absolute difference between its sum
     * and the specified goal is at least k.
     *
     * @param nums the input array of integers
     * @param goal the target integer sum for comparison
     * @param k the minimum required absolute difference
     * @return the total number of distant subarrays
     */
    public long distantSubarrays(int[] nums, int goal, int k) {
        long n = nums.length;
        long totalSubarrays = n * (n + 1) / 2;
        
        if (k == 0) {
            return totalSubarrays;
        }
        
        long[] prefixSums = new long[(int) n + 1];
        for (int i = 0; i < n; i++) {
            prefixSums[i + 1] = prefixSums[i] + nums[i];
        }
        
        long[] temp = new long[(int) n + 1];
        long complementaryCount = countComplementary(prefixSums, temp, 0, (int) n, goal, k);
        
        return totalSubarrays - complementaryCount;
    }

    private long countComplementary(long[] prefixSums, long[] temp, int left, int right, int goal, int k) {
        if (left >= right) {
            return 0;
        }
        
        int mid = left + (right - left) / 2;
        long count = countComplementary(prefixSums, temp, left, mid, goal, k);
        count += countComplementary(prefixSums, temp, mid + 1, right, goal, k);
        
        int p1 = left;
        int p2 = left;
        
        for (int j = mid + 1; j <= right; j++) {
            long lowerBound = prefixSums[j] - goal - k;
            long upperBound = prefixSums[j] - goal + k;
            
            while (p1 <= mid && prefixSums[p1] <= lowerBound) {
                p1++;
            }
            while (p2 <= mid && prefixSums[p2] < upperBound) {
                p2++;
            }
            
            count += (p2 - p1);
        }
        
        int i = left;
        int j = mid + 1;
        int index = left;
        
        while (i <= mid && j <= right) {
            if (prefixSums[i] <= prefixSums[j]) {
                temp[index++] = prefixSums[i++];
            } else {
                temp[index++] = prefixSums[j++];
            }
        }
        
        while (i <= mid) {
            temp[index++] = prefixSums[i++];
        }
        while (j <= right) {
            temp[index++] = prefixSums[j++];
        }
        
        for (i = left; i <= right; i++) {
            prefixSums[i] = temp[i];
        }
        
        return count;
    }
}