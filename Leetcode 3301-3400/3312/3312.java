// Leetcode 3312: Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/ 
// Solved on 17th of July, 2026
class Solution {
    /**
     * Counts the number of pairs (i, j) such that 1 <= i < j <= n and gcd(sum_odd(i..j), sum_even(i..j)) is odd.
     * @param nums an array of integers
     * @param queries an array of integers
     * @return the values of the queries
     */
    public int[] gcdValues(int[] nums, long[] queries) {
        int maxVal = 0;
        for (int num : nums) {
            if (num > maxVal) {
                maxVal = num;
            }
        }
        
        int[] counts = new int[maxVal + 1];
        for (int num : nums) {
            counts[num]++;
        }
        
        long[] exact = new long[maxVal + 1];
        for (int i = maxVal; i >= 1; i--) {
            long multipleCount = 0;
            for (int j = i; j <= maxVal; j += i) {
                multipleCount += counts[j];
            }
            long pairs = (multipleCount * (multipleCount - 1)) / 2;
            for (int j = 2 * i; j <= maxVal; j += i) {
                pairs -= exact[j];
            }
            exact[i] = pairs;
        }
        
        long[] prefix = new long[maxVal + 1];
        for (int i = 1; i <= maxVal; i++) {
            prefix[i] = prefix[i - 1] + exact[i];
        }
        
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            long target = queries[i];
            int low = 1;
            int high = maxVal;
            int match = 1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (prefix[mid] > target) {
                    match = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            result[i] = match;
        }
        
        return result;
    }
}