// Leetcode 4064: Longest Subarray Divisible by K with At Most One Negation II
// https://leetcode.com/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-ii/
// Solved on 31st of October, 2026
import java.util.Arrays;

class Solution {
    /**
     * Finds the length of the longest contiguous subarray that is valid.
     * A subarray is valid if its sum is divisible by k, or it can become divisible 
     * by k by negating at most one element within the subarray.
     *
     * @param nums the input array of integers
     * @param k the divisor
     * @return the length of the longest valid subarray, or 0 if no valid subarray exists
     */
    public int longestSubarray(int[] nums, int k) {
        int n = nums.length;
        int[] first = new int[k];
        int[] last = new int[k];
        
        for (int i = 0; i < k; i++) {
            first[i] = Integer.MAX_VALUE;
            last[i] = -1;
        }

        first[0] = 0;
        last[0] = 0;
        int currentPref = 0;
        
        for (int i = 1; i <= n; i++) {
            int val = nums[i - 1] % k;
            if (val < 0) {
                val += k;
            }
            currentPref = (currentPref + val) % k;
            
            if (first[currentPref] == Integer.MAX_VALUE) {
                first[currentPref] = i;
            }
            last[currentPref] = i;
        }

        int maxLen = 0;
        
        for (int r = 0; r < k; r++) {
            if (first[r] != Integer.MAX_VALUE && last[r] != -1) {
                if (last[r] - first[r] > maxLen) {
                    maxLen = last[r] - first[r];
                }
            }
        }

        int[] counts = new int[k];
        for (int i = 0; i < n; i++) {
            int val = nums[i] % k;
            if (val < 0) {
                val += k;
            }
            int x = (2 * val) % k;
            counts[x]++;
        }

        int[][] v = new int[k][];
        for (int i = 0; i < k; i++) {
            if (counts[i] > 0) {
                v[i] = new int[counts[i]];
            }
        }

        int[] ptrs = new int[k];
        for (int i = 0; i < n; i++) {
            int val = nums[i] % k;
            if (val < 0) {
                val += k;
            }
            int x = (2 * val) % k;
            v[x][ptrs[x]++] = i;
        }

        long[] packed = new long[k];
        for (int r = 0; r < k; r++) {
            packed[r] = (((long) first[r]) << 32) | r;
        }
        
        Arrays.sort(packed);
        
        int[] sortedR2 = new int[k];
        for (int i = 0; i < k; i++) {
            sortedR2[i] = (int) (packed[i] & 0xFFFFFFFFL);
        }

        for (int x = 0; x < k; x++) {
            if (counts[x] == 0) {
                continue;
            }
            
            int ptr = 0;
            for (int i = 0; i < k; i++) {
                int r2 = sortedR2[i];
                int firstPos = first[r2];
                
                if (firstPos == Integer.MAX_VALUE) {
                    break;
                }
                
                int r1 = (r2 + x) % k;
                int lastPos = last[r1];
                
                if (lastPos == -1 || firstPos >= lastPos) {
                    continue;
                }
                
                while (ptr < counts[x] && v[x][ptr] < firstPos) {
                    ptr++;
                }
                
                if (ptr < counts[x] && v[x][ptr] < lastPos) {
                    if (lastPos - firstPos > maxLen) {
                        maxLen = lastPos - firstPos;
                    }
                }
            }
        }

        return maxLen;
    }
}