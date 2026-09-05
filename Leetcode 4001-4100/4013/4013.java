// Leetcode 4013: Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/
// Solved on 5th of Spetember, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the number of valid subarrays where the ratio of even to odd elements 
     * is less than or equal to a given fraction a / b, and the number of odd elements is greater than zero.
     * This is achieved by transforming the array and using coordinate compression 
     * alongside a Fenwick tree to count valid prefix sum inversions.
     * 
     * @param nums the input array of integers
     * @param a the numerator of the ratio constraint
     * @param b the denominator of the ratio constraint
     * @return the total number of valid subarrays
     */
    public long countRatioSubarrays(int[] nums, int a, int b) {
        int n = nums.length;
        long[] prefixSums = new long[n + 1];
        long currentSum = 0;
        
        prefixSums[0] = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 == 0) {
                currentSum += b;
            } else {
                currentSum -= a;
            }
            prefixSums[i + 1] = currentSum;
        }
        
        long[] sortedSums = prefixSums.clone();
        Arrays.sort(sortedSums);
        
        int uniqueCount = 0;
        for (int i = 0; i <= n; i++) {
            if (i == 0 || sortedSums[i] != sortedSums[i - 1]) {
                sortedSums[uniqueCount++] = sortedSums[i];
            }
        }
        
        int[] fenwickTree = new int[uniqueCount + 1];
        long totalValidSubarrays = 0;
        
        for (int i = 0; i <= n; i++) {
            long targetSum = prefixSums[i];
            int low = 0;
            int high = uniqueCount - 1;
            int rank = 0;
            
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (sortedSums[mid] == targetSum) {
                    rank = mid + 1;
                    break;
                } else if (sortedSums[mid] < targetSum) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            
            int elementsLessThanCurrent = 0;
            int queryIndex = rank - 1;
            while (queryIndex > 0) {
                elementsLessThanCurrent += fenwickTree[queryIndex];
                queryIndex -= queryIndex & (-queryIndex);
            }
            
            totalValidSubarrays += (i - elementsLessThanCurrent);
            
            int updateIndex = rank;
            while (updateIndex <= uniqueCount) {
                fenwickTree[updateIndex] += 1;
                updateIndex += updateIndex & (-updateIndex);
            }
        }
        
        return totalValidSubarrays;
    }
}