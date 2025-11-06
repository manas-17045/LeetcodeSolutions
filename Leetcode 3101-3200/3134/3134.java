// Leetcode 3134: Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/
// Solved on 6th of November, 2025
import java.util.*;

class Solution {
    /**
     * Finds the median of the uniqueness array. The uniqueness array is formed by considering all possible subarrays
     * and counting the number of distinct elements in each subarray. The median is then the middle element of this sorted list of distinct counts.
     * @param nums The input array of integers.
     * @return The median of the uniqueness array.
     */
    public int medianOfUniquenessArray(int[] nums) {
        int n = nums.length;
        long total = (long)n * (n + 1) / 2;
        long target = (total + 1) / 2;
        int maxVal = 0;
        for (int v : nums){
            if (v > maxVal) {
                maxVal = v;
            }
        }
        int[] freq = new int[maxVal + 1];
        int low = 1;
        int high = n;
        int ans = n;
        while (low <= high) {
            int mid = (low + high) >>> 1;
            long cnt = countAtMost(nums, freq, mid);
            if (cnt >= target) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private long countAtMost(int[] nums, int[] freq, int k) {
        Arrays.fill(freq, 0);
        int left = 0;
        int distinct = 0;
        long count = 0;
        for (int right = 0; right < nums.length; right++) {
            int v = nums[right];
            if (freq[v] == 0){
                distinct++;
            }
            freq[v]++;
            while (distinct > k) {
                int u = nums[left++];
                freq[u]--;
                if (freq[u] == 0){
                    distinct--;
                }
            }
            count += right - left + 1;
        }
        return count;
    }
}