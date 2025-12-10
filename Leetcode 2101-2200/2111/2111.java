// Leetcode 2111: Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/
// Solved on 10th of December, 2025
class Solution {
    /**
     * Given a 0-indexed integer array arr and an integer k, return the minimum number of operations
     * to make arr k-increasing.
     * @param arr The input array.
     * @param k The interval for k-increasing subarrays.
     * @return The minimum number of operations.
     */
    public int kIncreasing(int[] arr, int k) {
        int n = arr.length;
        int longestNonDecreasing = 0;
        
        for (int i = 0; i < k; i++) {
            int[] tails = new int[n / k + 2];
            int size = 0;
            
            for (int j = i; j < n; j += k) {
                int val = arr[j];
                if (size == 0 || val >= tails[size - 1]) {
                    tails[size++] = val;
                } else {
                    int low = 0;
                    int high = size;
                    while (low < high) {
                        int mid = low + (high - low) / 2;
                        if (tails[mid] <= val) {
                            low = mid + 1;
                        } else {
                            high = mid;
                        }
                    }
                    tails[low] = val;
                }
            }
            longestNonDecreasing += size;
        }
        
        return n - longestNonDecreasing;
    }
}