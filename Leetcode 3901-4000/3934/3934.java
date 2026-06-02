// Leetcode 3934: Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/
// Solved on 2nd of June, 2026
import java.util.Arrays;

class Solution {
    /**
     * Finds the length of the smallest subarray that appears exactly once in the given array.
     * 
     * @param nums An array of integers.
     * @return The length of the smallest unique subarray.
     */
    public int smallestUniqueSubarray(int[] nums) {
        int n = nums.length;
        int low = 1;
        int high = n;
        int ans = n;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (hasUnique(mid, nums)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return ans;
    }

    private boolean hasUnique(int mid, int[] nums) {
        int n = nums.length;
        long[] hashes = new long[n - mid + 1];
        long h1 = 0;
        long h2 = 0;
        long p1 = 1;
        long p2 = 1;
        long m1 = 1000000007;
        long m2 = 1000000009;
        long b1 = 13331;
        long b2 = 100003;
        
        for (int i = 0; i < mid; i++) {
            h1 = (h1 * b1 + nums[i]) % m1;
            h2 = (h2 * b2 + nums[i]) % m2;
            if (i < mid - 1) {
                p1 = (p1 * b1) % m1;
                p2 = (p2 * b2) % m2;
            }
        }
        
        hashes[0] = (h1 << 32) | h2;
        
        for (int i = mid; i < n; i++) {
            h1 = (h1 - (nums[i - mid] * p1) % m1 + m1) % m1;
            h1 = (h1 * b1 + nums[i]) % m1;
            h2 = (h2 - (nums[i - mid] * p2) % m2 + m2) % m2;
            h2 = (h2 * b2 + nums[i]) % m2;
            hashes[i - mid + 1] = (h1 << 32) | h2;
        }
        
        Arrays.sort(hashes);
        
        int count = 1;
        for (int i = 1; i < hashes.length; i++) {
            if (hashes[i] == hashes[i - 1]) {
                count++;
            } else {
                if (count == 1) {
                    return true;
                }
                count = 1;
            }
        }
        
        return count == 1;
    }
}